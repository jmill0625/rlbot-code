# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.get_intent() is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        
        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            return
        
        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe_goal.location))    

        closest_boost = self.get_closest_large_boost()
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            return

        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_my_net' : (self.friend_goal.right_post, self.friend_goal.left_post) 
        }
        hits = find_hits(self,targets)
        if len(hits['at_opponent_goal']) > 0:
            self.set_intent(hits['at_opponent_goal'][0])
            print('at their goal')
            return
        if len(hits['away_from_my_net']) > 0:
            print('away from ouur goal')
            self.set_intent(hits['away_from_my_net'][0])
            return
        
       
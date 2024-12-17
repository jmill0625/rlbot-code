# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        available_boosts = [boost for boost in self.boosts if boost.large and boost.active]
        if self.get_intent() is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        
        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            print('rotating to goal')
        
            
        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post), 
        }
        hits = find_hits(self,targets)
        if len(hits['at_opponent_goal']) > 0:
            self.set_intent(hits['at_opponent_goal'][0])
            print('at their goal')
            return

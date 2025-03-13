from character import Character
import random

class Monster(Character):
    def __init__(self, base_strength=1):
        # Roll for combat strength and health points (these may be overwritten in main.py)
        rolled_combat = min(6, base_strength + random.randint(1, 6))
        rolled_hp = random.randint(1, 20)
        super().__init__(rolled_combat, rolled_hp)
    
    def monster_attacks(self, hero):
        ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(self.combat_strength) + 
              ") ---> Player (" + str(hero.health_points) + ")")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            hero.health_points -= self.combat_strength
            print("    |    The monster has reduced Player's health to: " + 
                  str(hero.health_points))
        return hero.health_points

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
from character import Character
import random

class Hero(Character):
    def __init__(self, base_strength=1):
        # Roll for combat strength and health points (these may be overwritten in main.py)
        rolled_combat = min(6, base_strength + random.randint(1, 6))
        rolled_hp = random.randint(1, 20)
        super().__init__(rolled_combat, rolled_hp)
    
    def hero_attacks(self, monster):
        ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
  """
        print(ascii_image)
        print("    |    Player's weapon (" + str(self.combat_strength) + 
              ") ---> Monster (" + str(monster.health_points) + ")")
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            monster.health_points -= self.combat_strength
            print("    |    You have reduced the monster's health to: " + 
                  str(monster.health_points))
        return monster.health_points

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
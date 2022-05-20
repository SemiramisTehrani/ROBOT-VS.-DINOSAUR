# week 4 : project
# 1- I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack ...
# ... method should lower a Robot’s health by the value of the Dinosaur’s attack_power. 
 
# 2- I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack ... 
# ... method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 

# 05/16/2022 : rev.1  --> not done

from fleet import Fleet
from herd import Herd


# watch the video session 

class Battlefield :
    
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()


    def run_game(self) :
     pass

    def display_welcome(self) :
        print('\nWelcome to an epic battle of ROBOT VS. DINOSAUR')

    def battle_phase(self):
            pass
    
    def display_winer(self):
        pass

        

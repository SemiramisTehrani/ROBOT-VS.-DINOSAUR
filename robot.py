# week 4 : project
# Robot to have a name, health, and active_weapon. 
# 05/16/2022 , rev.1 :init section
# 05/17/2022 , rev.2 : better init section
# 05/18/2022 , rev3  : working on the weapon selection , energy levle stuff, added dinosaur health check --> matching dinosaur class done?
# 5/20/2022 , rev 4 (101 session) : added random weapon list , moved dino health up
# 5/20/2022 , rev 4 (101 session) : final version

import random
from weapon import Weapon

class Robot : 
    def __init__(self , name) : 
       self.name = name                  # passed string
       self.health = 100                 # fix integer
       self.power  = 150                   # fix integer for now
       self.weapon_list = ["Laser", "Sonic" , "kinetic"] 
       
       self.active_weapon = Weapon(random.choice(self.weapon_list), 10)  

       pass
       
    def weapon_dinosaur(self, dinosaur) : 

        if dinosaur.health <= 0 :
                 print(f"\n{dinosaur.name} has been destroyed , end of game")

        if self.power > 10 :
            while True :

                weapon_selection = int(input(f" select option :  1 {self.weapon_list(0)} , 2 {self.weapon_list(1)} , 2 {self.weapon_list(3)}"))

                if weapon_selection == 1 : 
                    print(f'{self.weapon_list} attacked {dinosaur.name} with {self.weapon_list[0]}')
                    break
                
                elif weapon_selection == 2 :
                    print(f'{self.weapon_list} attacked {dinosaur.name} with {self.weapon_list[1]}')
                    break
                
                elif weapon_selection == 3 :
                    print(f'{self.weapon_list} attacked {dinosaur.name} with {self.weapon_list[2]}')
                    break

            self.power  = self.power - 10
            dinosaur.health = dinosaur.health - self.weapon_power
            print(f'{self.name} power is now {self.power}')
            print(f'{dinosaur.name} health is now {dinosaur.health}')
            

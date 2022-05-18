# week 4 : project
# Robot to have a name, health, and active_weapon. 
# 05/16/2022 , rev.1  :init section
# 05/17/2022 , rev.2  : better init section


from weapon import Weapon

class Robot : 
    def __init__(self , name) : 
       self.name = name                  # passed string
       self.health = 100                 # fix integer
       self.power= 150                   # fix integer for now
       self.active_weapon = Weapon()

       self.weapon_list = ["laser", "sonic" , "kinetic" ] 
       
    
    def attack_dinosaur(self, dinosaur) : 
        if self.power > 10 :
            while True :
        pass                                # void function


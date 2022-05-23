# week 4 : project (bonous) : list of 3 robots with 3 different weapon with 3 different atatck levle
# 05/20/2022 , rev.1 : created the file , 
# 05/20/2022 ,rev2 : weapon list should stay in the Robot class 
# 05/20/2022 ,rev2 : final version
# 
# 
# 1- importing Robot and Weapon class 
# 2- define init_fleet class
# 3- add methode to cover name and weapon and attack power list



from robot import Robot
from weapon import Weapon



class Fleet : 
    def __init__(self):
        self.robots = []
        self.fleet_of_robots()
        pass

    def fleet_of_robots(self):
        weapon1 = Weapon("Pulse Gun", 8)
        weapon2 = Weapon("Sonic gun", 15)
        weapon3 = Weapon("Laser Gun", 50)

        robot1 = Robot("Rosy", weapon1)
        robot2 = Robot("Angie", weapon2)
        robot3 = Robot("Pinky",  weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)    
        pass



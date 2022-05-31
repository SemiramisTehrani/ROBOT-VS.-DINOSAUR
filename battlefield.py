# week 4 : project
# 1- I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack ...
# ... method should lower a Robot’s health by the value of the Dinosaur’s attack_power. 
 
# 2- I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack ... 
# ... method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 

# 05/16/2022 : rev.1  --> not done
# 05/20/2022  rev2 : (afetr 101) : only importing fleet & herd ---> doesn't work this way

# 5/21/2022 rev.3 : work in progress 
# 5/22/2022 rev.4 : had to import robot and dinosaur classes here because couldn't fix the error. 
# 5/23/2022 rev.5 : still needs some print refienments & figure out why I had to added robot & dinosaur classes here. 
# 5/23/2022 rev.5 : runs with no error 
# reference : Googleing , github 

# 5/31/2022 : fixed typos and mismatchied variable names. 


import random
import robot
import dinosaur
from fleet import Fleet
from herd  import Herd



# 1- Battlefield class init is herd & fleet
# 2 - run game method : greeting , chossing team , battle , 

class Battlefield :                         # class is the whole book , methods are chapters
    
    def __init__(self):
        self.herd  = Herd()
        self.fleet = Fleet()
        pass

    def run_game(self) :
     self.display_greeting()                     # Greeting --> done
     self.team = self.choose_team()              # Choosing a team --> done
     self.battle()                               # battle
     
     self.ending()

    # greetings : cool way to print in the console (office hours video)
    def display_greeting(self) :
        print(
            """
********** 
Hello ! Welcome to battle of ROBOT VS. DINOSAUR
This is my frist project at Devcode Camp
Enjoy it. 

Game rules : 
                    Robot  Dinosaur 
Initial Health       100     100   
Initial Energy       150     150
Minimum Energy       10      10  

Robot is in Fleet group.
Dinosaur is in Herd group.

 **********
            """
            )

    def choose_team(self):
        choose_team = int(input("*** Choose your team: (1) Robots; (2) Dinosaurs***"))
        if choose_team == 1:
            print("*** You chose the fleet of Robots ***")
            return choose_team
        elif choose_team == 2:
            print("*** You chose the herd of Dinosaurs ***")
            return choose_team
        else:
            print("*** Invalid selection. Try again! ***")
            self.choose_team()
        pass 
        

    def battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print("*** Robots are here ***")
            first_turn = 1
        if first_turn == 2:
            print("*** Dinosaurs are here ***")
            first_turn = 2


        if first_turn == 1:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                    if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                        self.robo_turn()  # First turn team

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f"{self.herd.dinosaurs[0].name} is dead.")
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f"{self.fleet.robots[0].name} is dead.")
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return

                        self.dino_turn()  # Second turn team

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f"{self.herd.dinosaurs[0].name} is dead.")
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f"{self.fleet.robots[0].name} is dead.")
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return


        elif first_turn == 2:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                    if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                        self.dino_turn()  # First turn team

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f"{self.herd.dinosaurs[0].name} is dead.")
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f"{self.fleet.robots[0].name} is dead.")
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return

                        self.robo_turn()  # Second turn team

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f"{self.herd.dinosaurs[0].name} is dead.")
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f"{self.fleet.robots[0].name} is dead.")
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return

    def dino_turn(self):
        self.show_dino_opponent_options()
        self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])


    def robo_turn(self):
        self.show_robo_opponent_options()
        # print(" Here are Robots opponent list")
        self.fleet.robots[0].attack_dinosaur(self.herd.dinosaurs[0])
        # self.Robot.active_weapon.attack_dinosaur(self.herd.dinosaurs[0])
 


    def show_dino_opponent_options(self):
        i = 1
        for element in self.fleet.robots:
            print(f"{element.name} has {element.health} health.")
            i = i + 1


    def show_robo_opponent_options(self):
        i = 1
        for element in self.herd.dinosaurs:
            print(f"{element.name} has {element.health} health.")
            i = i + 1
    
    def display_winners_robots(self):

        if self.team == 1:
            print("**** winner ! The Robot fleet defeated the herd of Dinosaurs ****")
        if self.team == 2:
            print("**** loser ! The Robot fleet has defeated the herd of Dinosaurs ****")
        


    def display_winners_dinosaurs(self):

        if self.team == 2:
            print("**** winner! The herd of Dinosaurs has defeated the fleet of Robots.****")
        if self.team == 1:
            print("**** loser! The herd of Dinosaurs has defeated the fleet of Robots.****")

    def ending(self) :
        print ("*** Game is over ***")
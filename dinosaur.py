# week 4 : project
# Dinosaur to have a name, health, and attack power.  
# 05/16/2022 : rev.1 -->not done yet
# 05/17/2022 , rev.2  : better init section , working on the attack selection , energy levle stuff


class Dinosaur : 
    def __init__(self, name , attack_power) : 
       self.name = name                     # Dinosaur name: passed string
       self.attack_power = attack_power     # Dinosaur attack power levle : passed integer
       self.health =  100                   # Dinosaur health level = fix integer       
       self.energy =  200                   # Dinosaur energy level = fix integer 

       self.attack_list = ["Claw", "Bite" , "Fire-breathing" ]          # list counts from 0 


# start checking energy level (while : as long as energy stays above 10)
# 2- attack list selection
# 3- printing out the selected attack
# 4- decreasing energy by 10 step
# 5-  

    def attack_robot(self, robot) :
        if self.energy > 10 :
            while True :
                attack_selection = int(input(f" select option :  1 {self.attack_list(0)} , 2 {self.attack_list(1)} , 2 {self.attack_list(3)}"))

                if attack_selection == 1 : 
                    print(f'{self.attack_list} attacked {robot.name} with {self.attack_list[0]}')
                    break
                
                elif attack_selection == 2 :
                    print(f'{self.attack_list} attacked {robot.name} with {self.attack_list[1]}')
                    break
                
                elif attack_selection == 3 :
                    print(f'{self.attack_list} attacked {robot.name} with {self.attack_list[2]}')
                    break

            self.energy  = self.energy - 10
            robot.health = robot.health - self.attack_power
            print(f'{self.name} energy is now {self.energy}')
            print(f'{robot.name} health is now {robot.health}')


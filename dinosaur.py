# week 4 : project
# Dinosaur to have a name, health, and attack power.  
# 05/16/2022 : rev.1 -->not done yet
# 05/17/2022 , rev.2  : better init section , working on the attack selection , energy levle stuff
# 05/18/2022 , rev3 : added robot health check  ---> i think this one is done , making robot similar to this
# 5/20 /2022 , rev 4 ( 101 session): no need having while , moving up robot health
# 5/20 /2022 , rev 4 : final version


class Dinosaur : 
    def __init__(self, name , attack_power) : 
  
       self.name = name                     # Dinosaur name: passed string
       self.attack_power = attack_power     # Dinosaur attack power levle : passed integer
       # self.attack_power = 200
       self.health =  100                   # Dinosaur health level = fix integer       
       self.energy =  150                   # Dinosaur energy level = fix integer 

       self.attack_list = ["Claw", "Bite" , "Fire-breathing" ]          # list counts from 0 
       pass


# start checking energy level (while : as long as energy stays above 10) : maintain min energy level throughout the game
# 2- attack list selection by user
# 3- printing out the selected attack mode
# 4- D energy : decreasing energy by 10 units for example 
# 5- R health : R health - D attack power 
# 6- R health less than equal to 0 ---> print dead R 
# 7- printing D name with energy level
# 8- printing R name with energy level

    def attack_robot(self, robot) :

        if robot.health <= 0 :
                 print(f"\n{robot.name} has been destroyed , end of game")

        if self.energy > 10 :
            
                attack_selection = int(input(f" select option :  1 {self.attack_list(0)} , 2 {self.attack_list(1)} , 2 {self.attack_list(3)}"))

                if attack_selection == 1 : 
                    print(f'{self.attack_list} attacked {robot.name} with {self.attack_list[0]}')
                    
                
                elif attack_selection == 2 :
                    print(f'{self.attack_list} attacked {robot.name} with {self.attack_list[1]}')
                   
                
                elif attack_selection == 3 :
                    print(f'{self.attack_list} attacked {robot.name} with {self.attack_list[2]}')
                    


        self.energy  = self.energy - 10
        robot.health = robot.health - self.attack_power
        print(f'{self.name} energy is now {self.energy}')
        print(f'{robot.name} health is now {robot.health}')
           
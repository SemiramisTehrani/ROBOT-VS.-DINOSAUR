# week 4 : project (bonous) : list of 3 robots with 3 different weapon with 3 different atatck levle
# 05/20/2022 , rev.1 : created the file , 
# 5/20/2022 , rev.2 : final file
# 
# 
# 1- importing Dinosaur class 
# 2- define init_herd class
# 3- add methode to cover name and attack power list


from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.herd_of_dinosar()
        pass


    def herd_of_dinosar(self):
        dino1 = Dinosaur("Pink Tail", 8)
        dino2 = Dinosaur("Red Tail", 15)
        dino3 = Dinosaur("Purple Tail", 50)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
        pass
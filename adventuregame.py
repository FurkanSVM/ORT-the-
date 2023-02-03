
# 5 Treasures (‘T’), 5Monster (‘M’), 2 Sword (‘S’), 3 Potion (‘P’), and 3 Venom (‘V’)
import random
from random import randrange 
class game():
    def __init__(self):
        self.map=[[' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' ']]
        self.objects=["T","T","T","T","T","M","M","M","M","M","S","S","P","P","P","V","V","V"]
        self.points=0
        self.sword=0
        self.potion=0
        self.coordinates_of_hero=[]
        self.output_map=[[' ',' ',' ',' ',' ',' ',' '],
                         [' ',' ',' ',' ',' ',' ',' '],
                         [' ',' ',' ',' ',' ',' ',' '],
                         [' ',' ',' ',' ',' ',' ',' '],
                         [' ',' ',' ',' ',' ',' ',' '],
                         [' ',' ',' ',' ',' ',' ',' ']]
        self.sikis=0
        self.out_of_bounds=0
    def mapgenerator(self):
        for i in self.objects:
            while True:
                a=randrange(0,6)
                b=randrange(0,7)
                if self.map[a][b]==" ":
                    self.map[a][b]=i
                    break
                else:
                    continue
        while True:
           a=randrange(0,6)
           b=randrange(0,7)
           if self.map[a][b]==" ":
               self.map[a][b]="E"
               break
           else:
               continue
        for i in self.map:
            if "E" in i:
                row=self.map.index(i)
                column=i.index("E")
        self.coordinates_of_hero=[row,column]
        self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="E"
    def move(self,direction):
        self.out_of_bounds=0
        if direction=="U":
            if self.coordinates_of_hero[0]==0:
                self.coordinates_of_hero[0]=0
                self.out_of_bounds=1
            else:
                self.coordinates_of_hero[0]-=1
        if direction=="D":
            if self.coordinates_of_hero[0]==5:
                self.coordinates_of_hero[0]=5
                self.out_of_bounds=1
            else:
                self.coordinates_of_hero[0]+=1
        if direction=="L":
            if self.coordinates_of_hero[1]==0:
                self.coordinates_of_hero[1]=0
                self.out_of_bounds=1
            else:
                self.coordinates_of_hero[1]-=1
        if direction=="R":
            if self.coordinates_of_hero[1]==6:
                self.coordinates_of_hero[1]=6
                self.out_of_bounds=1
            else:
                self.coordinates_of_hero[1]+=1
    def adventure(self):
        
        if self.sikis==0:   # first 
            
            print(self.output_map[0])
            print(self.output_map[1])
            print(self.output_map[2])
            print(self.output_map[3])
            print(self.output_map[4])
            print(self.output_map[5])
            print(" ")
            print(" ")
    
       
        direction=input("Press L U R D to move: ")
        note=""
        dead=0
        
        self.move(direction)       
        

        if self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]!=" ":  # geçtiği yola dönerse
            note+="You can't move there!"
            if self.out_of_bounds==0:
                if direction == "U":
                    self.coordinates_of_hero[0]+=1
                if direction == "L":
                    self.coordinates_of_hero[1]+=1
                if direction == "D":
                    self.coordinates_of_hero[0]-=1
                if direction == "R":
                    self.coordinates_of_hero[1]-=1
        else:
            
            if self.map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]==" ":  # bi sey yoksa
                self.points+=1
                self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="E"


            if self.map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]=="M":  # monster
                if self.sword==0:
                    note+="Oh no! Monster!, you die"
                    self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="M"

                    dead=1             
                else:
                    note+="Oh no! Monster!  Sword is used."
                    self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="M"
                    self.sword-=1
                    self.points+=1


            if self.map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]=="V":  # venom
                if self.potion==0:
                    note+="Oh no! VENOM!, you die"
                    self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="V"

                    dead=1                 
                else:
                    note+="Oh no! VENOM!  Potion is used."
                    self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="V"
                    self.potion-=1
                    self.points+=1


            if self.map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]=="T":  # treasure
                note+="+TREASURE"
                self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="T"
                self.points+=2


            if self.map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]=="P":  # potion
                note+="+POTION"
                self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="P"
                self.points+=1
                self.potion+=1


            if self.map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]=="S":  # sword
                note+="+SWORD"
                self.output_map[self.coordinates_of_hero[0]][self.coordinates_of_hero[1]]="S"
                self.points+=1
                self.sword+=1
         
        print("\033[H\033[J", end="")
        print(self.output_map[0])
        print(self.output_map[1])
        print(self.output_map[2])
        print(self.output_map[3])
        print(self.output_map[4])
        print(self.output_map[5])
        print(" ")
        print(note)
        print(" ")     
        print("Swords:",[self.sword],end="      ")
        print("Potions:",[self.potion],end="      ")
        print("Points:",[self.points])
        print(" ")

        if dead==0:
            self.sikis=1
            self.adventure()
        else:
            return 


# map[y][x]   y:0,1,2,3,4,5  x=0,1,2,3,4,5,6
odyssey=game()
odyssey.mapgenerator()
odyssey.adventure()
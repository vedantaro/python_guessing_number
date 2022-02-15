#--------------------------------------------------------------------------------------------------------------------------------------
from random import randint, random               #libraries
import os
#-------------------------------------------------------------------------------------------------------------------------------------
class Random_number():                          #class
    computer_guess= randint(1,10)
#--------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):    
        self.user_guess=0
        self.number_guess_time=0               #constructor
        self.computer_guess= randint(1,10)
        self.user_play=0
#--------------------------------------------------------------------------------------------------------------------------------------
    def game_mechanics(self):                 #function
#--------------------------------------------------------------------------------------------------------------------------------------
        self.user_guess= int(input("choose a number between 1 to 10: "))
        print(" ")
        self.number_guess_time+=1
        while (self.user_guess >10):
            if self.user_guess>10:
                self.user_guess=int(input("you have choosen wrong number , choose wisely between 1 to 10: "))
                self.number_guess_time+=1 
        print(" ")
#--------------------------------------------------------------------------------------------------------------------------------------
        while(self.user_guess!=self.computer_guess):
#--------------------------------------------------------------------------------------------------------------------------------------            
            if self.user_guess<self.computer_guess:
                print("the number %d is smaller choose a larger number. the number guessed time %d" % (self.user_guess,self.number_guess_time))
                self.user_guess= int(input("try again!! choose number between 1 to 10: "))
                self.number_guess_time+=1
                print(" ")    
                while (self.user_guess >10):
                    if self.user_guess>10:
                        self.user_guess=int(input("you have choosen wrong number , choose wisely between 1 to 10: "))
                        self.number_guess_time=+1
#--------------------------------------------------------------------------------------------------------------------------------------
            if self.user_guess>self.computer_guess:
                print("the number %d is greater choose a smaller number. the number guessed time %d" % (self.user_guess,self.number_guess_time))
                self.user_guess= int(input("try again!! choose number between 1 to 10: "))
                self.number_guess_time+=1
                print(" ")    
                while (self.user_guess >10):
                    if self.user_guess>10:
                        self.user_guess=int(input("you have choosen wrong number , choose wisely between 1 to 10: "))
                        self.number_guess_time=+1
#--------------------------------------------------------------------------------------------------------------------------------------            
        if self.user_guess==self.computer_guess:
            self.user_play=int(input("congragulations!!, you guessed the correct number in %d times. press 1 to  play again & press 2 to quit: "% self.number_guess_time))
            print(" ")
            if self.user_play==1 or self.user_play==2:
                new_game()
#--------------------------------------------------------------------------------------------------------------------------------------                     

def new_game():
    user_play=int(input("press 1 to play press 2 to quit :"))
    if user_play==1:   #function to recall the game & to quit
        Random_number()                  #function not recalling the game, idk why , but succesful in quiting the game
    else:
        os._exit(2)       
new_game() 
#--------------------------------------------------------------------------------------------------------------------------------------           
r= Random_number()                                  #instance of class
#--------------------------------------------------------------------------------------------------------------------------------------
r.game_mechanics()  

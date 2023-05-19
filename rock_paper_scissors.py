#Rock Paper Scissors Game
#It is an intransitive hand game, usually played between two people, in which each player
# simultaneously forms one of three shapes with an outstretched hand

#Start by selecting your choice either rock, paper or scissors
#Computer choose its own choice by randomly selecting one of the shapes(random)
#If your choice matches with that of the computer you play the game again(while loop)
#If your choice is rock and the computer's choice is scissors you win, if your choice is paper
#and the computer's choice is rock you win and if your choice is scissors and the computer's
#choice is paper you win.
#Create a blueprint for the game by using classes.
import random


class Rps:
    shapes = ["rock","paper","scissors"]
    def __init__(self,choice:str):
        self.choice = choice.lower()

    @classmethod
    def comp_choicef(cls):
        Rps.comp_choice = random.choice(Rps.shapes)
        return Rps.comp_choice

    def play_game(self):
        self.computer = Rps.comp_choicef()
        if self.choice in Rps.shapes:
            print("Computer's choice: ", self.computer)
            if self.choice == "paper" and self.computer == "rock" or self.choice == "rock" \
                    and self.computer == "scissors" or self.choice == "scissors" and \
                    self.computer == "paper":
                print("You win")

            elif self.choice == self.computer:
                print("No winners")

            else:
                print("Computer wins")
        else:
            print("Shape must be spelt correctly")



print("*****Welcome to the Rock Paper Scissors Game *****")
print("*****Select either rock, paper or scissors****")
my_choice = input("Input your choice: ")
game = Rps(my_choice)
game.play_game()







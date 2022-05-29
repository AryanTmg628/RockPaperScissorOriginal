''' In this file we are going to run our main program we will ask for the name of two users in this script
and
-- we will need random choice from the computer we will import it from RandomChoice module

#writing an algorithm for scissor paper rock
1. Ask for the name of user
2. Display the welcome page
3. Creating variables named userCount and computerCount to count the number of games win by them respectively
4. We will play 3 rounds
5. Opening loop for 3 times
6. Create a varaible named choiceOfUser and ask user its answer(rock or paper or scissor)
7. create another varaible named choiceOfComputer and import from RandomChoice module
8. If choiceOfUser is equalsnto the choiceOfCOmputer then it's draw
9. Elif choiceOfUser is rock and choiceOfOmputer is scissor then increment the userCount since he win first round and continue to the second round and viceversa
10. Elif choiceOfUser is paper and choiceOfCOmputer is scissor then increment the computerCount and viceversa
11. Compare userCount and computerCount
12 If userCOunt > then userwins
13. else computerwins

'''
from os import system
from time import sleep
import RandomChoice
import pyttsx3


#creating the instance
engine = pyttsx3.init()

#defning the speak functin
def speak(text) :

    engine.say(text)
    engine.runAndWait()

#defining the welcomePage function
def welcomePage(userName) :

    system("CLS")
    print("\n"*3 + "\t"*5 + "-"*5 + " WELCOME TO ROCK PAPER AND SCISSOR " + "-"*5)

    #delaying the time for 2 seconds
    sleep(2)

    #greeting the user using Voice Assistant 
    speak("Hello , Mr {}. We welcome you to Rock Paper and Scissor Game..".format(userName))

    #confirming to play
    confirmation = input("\n"*3 + "\t"*5 + "Do you want to continue or exit (PRESS C For Continue and E for exit) : ")

    if confirmation == "E" :
        exit(0)

    


if __name__ == "__main__" :

    system("CLS")

    #asking for the name of the user 
    nameOfUser = input("\n"*3 + "\t"*6 + "Enter your name : ")

    #invoking the welcome page function
    welcomePage(nameOfUser)

    #creating variable named UserCount and ComputerCount and intializing with 0 it counts the number of rounds win by them
    userCount = 0
    computerCount = 0

    #informing the uses that we will be playing 3 rounds
    noOfRounds = 3
    system("CLS")
    print("\n"*3 + "\t"*5 + '''We will be playing 3 rounds \n
                    \t\t\t\t\t Who wins most round will win the game''')

    #starting the loop
    for i in range(noOfRounds) :
 
        #printing the round name  and choices
        print("\n"*2 + "\t"*5 + "Round {}".format(i+1))
        print("\n"*2) #printing two new lines
        print("\n"*1 + "\t"*5 + "Choices : Rock, Paper, Scissor")

        #creating the choiceOfUser and choiceOfComputer variables
        choiceOfUser = input("\n"*2 + "\t"*3 + "Enter your choice {} : ".format(nameOfUser))
        choiceOfComputer = RandomChoice.getRandomChoice()

        #Displaying their choices and comparing them

        print("\n" + "{} choice is {}".format(nameOfUser,choiceOfUser))
        print("\n" + "{} choice is {}".format("Computer",choiceOfComputer))

        #Draw conditions
        if (choiceOfUser.lower() == "rock" and choiceOfComputer.lower() == "rock") or (choiceOfUser.lower() == "paper" and choiceOfComputer.lower() == "paper") or (choiceOfUser.lower() == "scissor" and choiceOfComputer.lower() == "scissor") :
            print("\n"+ "\t"*3 + "Draw........")
        #user winning conditions

        elif (choiceOfUser.lower() == "rock" and choiceOfComputer.lower() == "scissor") or (choiceOfUser.lower() == "paper" and choiceOfComputer.lower() == "rock") or (choiceOfUser.lower() == "scissor" and choiceOfComputer.lower() == "paper") :
            print("\n"+ "\t"*3 + "{} wins.".format(nameOfUser))
            userCount +=1 #increment the userCount by 1

        else :

            print("\n" + "\t"*3 + "{} wins.".format("Computer"))
          
            computerCount += 1 #increment of computercount by 1

        
        #delay time for 3 second
        sleep(3)

    #Comparing userCOunt and ComputerCount

            #draw
    if userCount == computerCount :
        print("\n"*4 + "\t"*5 + "This game is Draw.............")
        sleep(2)
        exit(0)

            #user wins
    elif userCount > computerCount :

        print("\n"*4 + "\t"*5 + "{} wins the game............".format(nameOfUser))
        sleep(2)
        exit(0)

            #computer wins
    else :

        print("\n"*4 + "\t"*5 + "{} wins the game.............".format("Computer"))
        sleep(2)
        exit(0)

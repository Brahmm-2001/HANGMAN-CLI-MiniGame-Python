'''
-----------------------------

    H A N G M A N

-----------------------------

Code By : YUVRAJ

'''

import os
import msvcrt
import random
import string


def SHOW_HANGMAN(step):

    if step == 0:
        print("\n")
        print("\t\t\t       ||-------/-------")
        print("\t\t\t       ||      /")
        print("\t\t\t       ||     /")
        print("\t\t\t       ||    /")
        print("\t\t\t       ||   /")
        print("\t\t\t       ||  /")
        print("\t\t\t       || /")
        print("\t\t\t       ||/")
        print("\t\t\t       |/")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 1:
        print("\n")
        print("\t\t\t       ||-------/-------------------------------")
        print("\t\t\t       ||      /")
        print("\t\t\t       ||     /")
        print("\t\t\t       ||    /")
        print("\t\t\t       ||   /")
        print("\t\t\t       ||  /")
        print("\t\t\t       || /")
        print("\t\t\t       ||/")
        print("\t\t\t       |/")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 2:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /")
        print("\t\t\t       ||   /")
        print("\t\t\t       ||  /")
        print("\t\t\t       || /")
        print("\t\t\t       ||/")
        print("\t\t\t       |/")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 3:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /               /|||||\\")
        print("\t\t\t       ||   /               * -- -- *")
        print("\t\t\t       ||  /                *  ___  *")
        print("\t\t\t       || /                  *--_--*")
        print("\t\t\t       ||/")
        print("\t\t\t       |/")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 4:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /               /|||||\\")
        print("\t\t\t       ||   /               * -- -- *")
        print("\t\t\t       ||  /                *  ___  *")
        print("\t\t\t       || /                  *--_--*")
        print("\t\t\t       ||/                      |")
        print("\t\t\t       |/                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 5:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /               /|||||\\")
        print("\t\t\t       ||   /               * -- -- *")
        print("\t\t\t       ||  /                *  ___  *")
        print("\t\t\t       || /                  *--_--*")
        print("\t\t\t       ||/                      |")
        print("\t\t\t       |/                      /|")
        print("\t\t\t       ||                     / |")
        print("\t\t\t       ||                    /  |")
        print("\t\t\t       ||                   /   |")
        print("\t\t\t       ||                  *    |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 6:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /               /|||||\\")
        print("\t\t\t       ||   /               * -- -- *")
        print("\t\t\t       ||  /                *  ___  *")
        print("\t\t\t       || /                  *--_--*")
        print("\t\t\t       ||/                      |")
        print("\t\t\t       |/                      /|\\")
        print("\t\t\t       ||                     / | \\")
        print("\t\t\t       ||                    /  |  \\")
        print("\t\t\t       ||                   /   |   \\")
        print("\t\t\t       ||                  *    |    *")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t       ||")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 7:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /               /|||||\\")
        print("\t\t\t       ||   /               * -- -- *")
        print("\t\t\t       ||  /                *  ___  *")
        print("\t\t\t       || /                  *--_--*")
        print("\t\t\t       ||/                      |")
        print("\t\t\t       |/                      /|\\")
        print("\t\t\t       ||                     / | \\")
        print("\t\t\t       ||                    /  |  \\")
        print("\t\t\t       ||                   /   |   \\")
        print("\t\t\t       ||                  *    |    *")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                      /")
        print("\t\t\t       ||                     /")
        print("\t\t\t       ||                    /")
        print("\t\t\t       ||                   /")
        print("\t\t\t       ||                  /")
        print("\t\t\t       ||                 *")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")

    elif step == 8:
        print("\n")
        print("\t\t\t       ||-------/--------------(|)--------------")
        print("\t\t\t       ||      /                |")
        print("\t\t\t       ||     /                 |")
        print("\t\t\t       ||    /               /|||||\\")
        print("\t\t\t       ||   /               * -- -- *")
        print("\t\t\t       ||  /                *  ___  *")
        print("\t\t\t       || /                  *--_--*")
        print("\t\t\t       ||/                      |")
        print("\t\t\t       |/                      /|\\")
        print("\t\t\t       ||                     / | \\")
        print("\t\t\t       ||                    /  |  \\")
        print("\t\t\t       ||                   /   |   \\")
        print("\t\t\t       ||                  *    |    *")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                       |")
        print("\t\t\t       ||                      / \\")
        print("\t\t\t       ||                     /   \\")
        print("\t\t\t       ||                    /     \\")
        print("\t\t\t       ||                   /       \\")
        print("\t\t\t       ||                  /         \\")
        print("\t\t\t       ||                 *           *")
        print("\t\t\t__\|/__||___________________________________________")
        print("\n")


def Help(mode):
    
    os.system("cls")
    print("\n\t\t\t\t/---------------\\")
    print("\t\t\t\t|      HELP     |")
    print("\t\t\t\t\\---------------/")

    if mode == 1:
        print("\n\n\n\t\t\tThis is Single Player Mode.")
        print("\n\t\t\tIn thid Mode, the Player would have to Guess a Word using a given Hint.")
        print("\n\t\t\tPlayer will be asked to Guess a letter of the word.")
        print("\n\t\t\tIf the Guessed letter is present in the Word, all the occurrence of the in the Word will be displayed.")
        print("\n\t\t\tAnd if the Guessed letter is incorrect, the process of Hanging a Man will get started.")
        print("\n\t\t\tIf the Word is Guessed correctly, the Player will WIN.")
        print("\n\t\t\tOtherwise, the Man will be Hanged & the GAME will be OVER.")
        print("\n\t\t\tFollowing Image shows the HANGED MAN, the step where the GAME will get OVER.")
        SHOW_HANGMAN(8)
    
    if mode == 2:
        print("\n\n\n\t\t\tThis is Two Player Mode.")
        print("\n\t\t\tIn thid Mode, one of the Player will give the hint to Guess a Word to other.")
        print("\n\t\t\tThere will be as many Rounds as You want.")
        print("\n\t\t\tPlayer will be asked to Guess a letter of the word.")
        print("\n\t\t\tIf the Guessed letter is present in the Word, all the occurrence of the in the Word will be displayed.")
        print("\n\t\t\tAnd if the Guessed letter is incorrect, the process of Hanging a Man will get started.")
        print("\n\t\t\tIf the Word is Guessed correctly, the Player will be awarded a Point.")
        print("\n\t\t\tOtherwise, the Man will be Hanged & no Points will be awarded.")
        print("\n\t\t\tAt the End of Five Rounds, Player scored highest Points will WIN.")
        print("\n\t\t\tFollowing Image shows the HANGED MAN, the step where the GAME will get OVER.")
        SHOW_HANGMAN(8)

    print("\n\n\n\t\t\tPress ENTER to START the GAME........", end = "")
    msvcrt.getwch()


def print_alphabets(alphabets):
    print("\n\n\n\t\t\t", end = "")
    i = 1
    for letter in alphabets:
        if i == 7 or i == 13 or i == 19 or i == 25:
            print("\n\t\t\t", end = "")
        print(letter, end = " ")
        i = i + 1


def START_GAME(player_name, hint, word, mode):

    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    mistake = 0
    temp_word = ""
    for i in range(len(word)):
        temp_word = temp_word + " "

    while mistake <= 7:
        os.system("cls")
        print("\n\n")
        print("\t\t\t\t/------------------------\\")
        print("\t\t\t\t|      H A N G M A N     |")
        print("\t\t\t\t\\------------------------/")
        SHOW_HANGMAN(mistake)
        print("\n\t\t\tHint : " + hint)
        print("\n\t\t\t", end = "")
        for letter in temp_word:
            if not letter.isalpha():
                print("__", end = " ")
            else:
                print(letter, end = " ")
        print_alphabets(alphabets)
        while(1):
            character = input("\n\n\t\t\t" + player_name + ", Guess a Character (Choose from the alphabets given above) : ")
            if character.isalpha() and character in alphabets:
                break
            else:
                print("\n\t\t\t     Invalid Character !!!")
        alphabets[alphabets.index(character)] = "-"
        if character in word:
            temp_word = list(temp_word)
            for i in range(len(word)):
                if word[i] == character:
                    temp_word[i] = character
            temp_word = "".join(temp_word)
            temp_word = str(temp_word)
        else:
            mistake = mistake + 1

        if  temp_word == word:
            os.system("cls")
            print("\n\n\t\t\t\t/------------------------\\")
            print("\t\t\t\t|      H A N G M A N     |")
            print("\t\t\t\t\\------------------------/")
            SHOW_HANGMAN(mistake)
            print("\n\n\t\t\tCONGRATULATIONS !")
            print("\n\n\t\t\tThe Word is : " + word + ".")
            print("\n\t\t\t" + player_name + ", You Guessed the Right Word.")
            print("\n\t\t\tYou WIN !!!")
            print("\n\n\n\t\t\tPress Any Key to CONTINUE", end = "")
            msvcrt.getwch()
            if mode == 2:
                return 1
            else:
                return
        
    os.system("cls")
    print("\n\n\t\t\t\t/------------------------\\")
    print("\t\t\t\t|      H A N G M A N     |")
    print("\t\t\t\t\\------------------------/")
    SHOW_HANGMAN(mistake)                
    print("\n\n\t\t\tGAME OVER !!!!")
    print("\n\n\t\t\tThe Word is : " + word + ".")
    print("\n\t\t\t" + player_name + ", You LOSE !!")
    print("\n\n\n\t\t\tPress Any Key to CONTINUE", end = "")
    msvcrt.getwch()
    if mode == 2:
        return 0
    else:
        return


def P_V_C():
    Help(1)
    os.system("cls")
    print("\n\n")
    print("\t\t\t\t/------------------------\\")
    print("\t\t\t\t|      H A N G M A N     |")
    print("\t\t\t\t\\------------------------/")
    print("\n\n")
    while(1):
        player_name = input("\n\t\t\tPlayer, Please Enter Your Name : ")
        if len(player_name) > 0:
            break
        else:
            print("\n\t\t\tInvalid Name !!!")
    Word_dict = ({"FOOD" : ["PANCAKE", "CUPCAKE", "EGG", "BIRIYANI", "NOODLES", "MOMO"],
                "FESTIVAL" : ["DIWALI", "HOLI", "EID", "LOHRI", "DURGAPUJA"],
                "MUSIC" : ["PIANO", "GUITAR", "VIOLEN", "DRUMKIT", "TABLA"],
                "PROFESSION" : ["LAWYER", "OFFICER", "DOCTOR", "SCIENTIST", "ENGINEER"],
                "VEHICLE" : ["BIKE", "CAR", "BUS", "CYCLE", "RIKSHAW"]})
    hint = random.choice(list(Word_dict.keys()))
    word = random.choice(Word_dict[hint])
    print("\n\n\n\t\t\tPress ENTER to START the GAME........", end = "")
    msvcrt.getwch()
    START_GAME(player_name, hint, word, None)

def SHOW_POINTS():
    pass

def P_V_P():
    Help(2)
    os.system("cls")
    print("\n\n")
    print("\t\t\t\t/------------------------\\")
    print("\t\t\t\t|      H A N G M A N     |")
    print("\t\t\t\t\\------------------------/")
    print("\n\n")
    while(1):
        p1_name = input("\n\t\t\tPlayer 1, Please Enter Your Name : ")
        if len(p1_name) > 0:
            break
        else:
            print("\n\t\t\tInvalid Name !!!")
    while(1):
        p2_name = input("\n\n\n\t\t\tPlayer 2, Please Enter Your Name : ")
        if len(p2_name) > 0:
            break
        else:
            print("\n\t\t\tInvalid Name !!!")
    while(1):
        Rounds = input("\n\n\n\t\t\tHow many Rounds You both want to Play ? : ")
        if Rounds.isdigit() and len(Rounds) > 0:
            Rounds = int(Rounds)
            break
        else:
            print("\n\t\t\tInvalid Value !!!")
    p1_points = 0
    p2_points = 0
    Round = 1
    while Round <= Rounds:

        os.system("cls")
        print("\n\n")
        print("\t\t\t\t/------------------------\\")
        print("\t\t\t\t|      H A N G M A N     |")
        print("\t\t\t\t\\------------------------/")
        print("\n\n\n\t\t\tROUND : " + str(Round))
        while(1):
            word = input("\n\n\t\t\t" + p2_name + ", Enter the Word that You want to be Guessed by " + p1_name + " : ")
            if len(word) > 0:
                break
            else:
                print("\n\t\t\tInvalid Word !!!")
        while(1):
            hint = input("\n\t\t\t" + p2_name + ", Enter the Hint : ")
            if len(hint) > 0:
                break
            else:
                print("\n\t\t\tInvalid Hint !!!")
        print("\n\n\n\t\t\tPress ENTER to START the GAME........", end = "")
        msvcrt.getwch()
        p1_points = p1_points + START_GAME(p1_name, hint, word.upper(), 2)

        os.system("cls")
        print("\n\n")
        print("\t\t\t\t/------------------------\\")
        print("\t\t\t\t|      H A N G M A N     |")
        print("\t\t\t\t\\------------------------/")
        print("\n\n\n\t\t\tROUND : " + str(Round))
        while(1):
            word = input("\n\n\t\t\t" + p1_name + ", Enter the Word that You want to be Guessed by " + p2_name + " : ")
            if len(word) > 0:
                break
            else:
                print("\n\t\t\tInvalid Word !!!")
        while(1):
            hint = input("\n\t\t\t" + p1_name + ", Enter the Hint : ")
            if len(hint) > 0:
                break
            else:
                print("\n\t\t\tInvalid Hint !!!")
        print("\n\n\n\t\t\tPress ENTER to START the GAME........", end = "")
        msvcrt.getwch()
        p2_points = p2_points + START_GAME(p2_name, hint, word.upper(), 2)

        Round = Round + 1
    
    
    os.system("cls")
    print("\n\n")
    print("\t\t\t\t/------------------------\\")
    print("\t\t\t\t|      H A N G M A N     |")
    print("\t\t\t\t\\------------------------/")
    print("\n\n")
    print("\t\t\tSCORES :-")
    print("\n\n\t\t\t" + p1_name + " : " + str(p1_points))
    print("\n\t\t\t" + p2_name + " : " + str(p2_points))
    print("\n\n\t\t\tCONGRATULATIONS !")
    if p1_points > p2_points:
        print("\n\t\t\t" + p1_name + " WINS the GAME.")
    elif p2_points > p1_points:
        print("\n\t\t\t" + p2_name + " WINS the GAME.")
    else:
        print("\n\t\t\tDRAW !!! No one WINS !!!")
    print("\n\n\n\t\t\tPress ENTER to START the GAME........", end = "")
    msvcrt.getwch()


def PLAY_MODES():

    while(1):
    
        os.system("cls")

        print("\n\n")
        print("\t\t\t\t/------------------------\\")
        print("\t\t\t\t|      H A N G M A N     |")
        print("\t\t\t\t\\------------------------/")
        print("\n\n")
        print("\t\t\t/--------------------------------------\\")
        print("\t\t\t|                                      |")
        print("\t\t\t|  Modes :                             |")
        print("\t\t\t|                                      |")
        print("\t\t\t|      1. Player V/S Computer          |")
        print("\t\t\t|                                      |")
        print("\t\t\t|      2. Player V/S Player            |")
        print("\t\t\t|                                      |")
        print("\t\t\t|                                      |")
        print("\t\t\t|  << Exit - ( Press any Key )         |")
        print("\t\t\t|                                      |")
        print("\t\t\t\\--------------------------------------/")
        print("\n\n\t\t\t       Choose Your Option - ", end = "")
        mode = msvcrt.getwch()
        if mode == "1":
            P_V_C()
        elif mode == "2":
            P_V_P()
        else:
            print("\n\n\t\t\t       Are You sure to EXIT ?")
            print("\t\t\t       Predd - 1 to CONFIRM | Any Key to CANCEL : ", end = "")
            confirm = msvcrt.getwch()
            if confirm == "1":
                print("\n")
                exit(0)
            else:
                continue


def Play_HANGMAN():

    while(1):
        os.system("cls")
        print("\n\n")
        print("")
        print("       ||-------/--------------(|)--------------         |    ")
        print("       ||      /                |                        |    |__|")
        print("       ||     /                 |                        |    |  |")
        print("       ||    /               /|||||\\                     |    ")
        print("       ||   /               * -- -- *                    |     /_|")
        print("       ||  /                *  ___  *                    |    /  |")
        print("       || /                  *--_--*                     |    ")
        print("       ||/                      |                        |    |\\ |\t-----------")
        print("       |/                      /|\\                       |    | \\|\t| P L A Y |  ( Press 1 )")
        print("       ||                     / | \\                      |        \t-----------")
        print("       ||                    /  |  \\                     |     / _")
        print("       ||                   /   |   \\                    |    /_|")
        print("       ||                  *    |    *                   |        \t-----------")
        print("       ||                       |                        |    |\\/|\t| E X I T |  ( Press Any Key )")
        print("       ||                       |                        |    |  |\t-----------")
        print("       ||                       |                        |    ")
        print("       ||                      / \\                       |     /_|")
        print("       ||                     /   \\                      |    /  |")
        print("       ||                    /     \\                     |    ")
        print("       ||                   /       \\                    |    |\\ |")
        print("       ||                  /         \\                   |    | \\|")
        print("       ||                 *           *                  |    ")
        print("__\|/__||____________________________________________    |    ")
        print("\n\n")
        print("\t\t\t\t\tChoose Your Option...........", end = "")
        choice = msvcrt.getwch()
        if choice == "1":
            PLAY_MODES()
        else:
            print("\n\n\t\t\t\t\t       Are You sure to EXIT ?")
            print("\t\t\t\t\t       Press - 1 to CONFIRM | Any Key to CANCEL : ", end = "")
            confirm = msvcrt.getwch()
            if confirm == "1":
                print("\n")
                exit(0)
            else:
                continue


Play_HANGMAN()
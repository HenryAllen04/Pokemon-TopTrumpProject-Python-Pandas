import numpy as np
import pandas as pd
import random
import ShuffleStats as SS
import BattleForms as BF

def readyup():
    ready = input("#READY UP!#\n y/n: ")
    ready = ready.upper()
    val = False
    if ready == ('Y'):
        val = True
        battle()
    if ready == ('N'):
        val = True
        #add show again
        readyup()
    elif val == False:
        print("\nmust enter y/n")
        readyup()
       

def battle():
    val = True
    while val == True:
        BF.rounds()
        print("\n#CHOOSE BATTLE STAT#")
        def prompt():
            global x
            try:
                x = int(input("\nEnter Here: "))
                if x not in range(1,7):
                    print("\n#CHOOSE STAT NUMBER#\n")
                    SS.statchoice()
                    prompt()
                else:
                    pass
            except:
                print("\n#CHOOSE STAT NUMBER#\n")
                SS.statchoice()
                prompt()

        prompt()   

        if x == 1:
            BF.HP_vs_HP()
        elif x == 2:
            BF.ATTACK_vs_ATTACK()
        elif x == 3:
            BF.DEFENSE_vs_DEFENSE()
        elif x == 4:
            BF.SP_ATK_vs_SP_ATK()
        elif x == 5:
            BF.SP_DEF_vs_SP_DEF()
        else:
            BF.SPEED_vs_SPEED()

        user_deck_df = pd.read_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv')
        AI_deck_df = pd.read_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv')

        if len(user_deck_df) == 10:
            print("----------------------------------------")
            print("             YOU WIN! :)")
            print("----------------------------------------")
            val = False
        elif len(AI_deck_df) == 10:
            print("----------------------------------------")
            print("             YOU LOST :(")
            print("----------------------------------------")
            val = False
        else:
            pass
    

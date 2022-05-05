import numpy as np
import pandas as pd
import random

df = pd.read_csv('pokemon_data.csv')

def shuffle():
    for i in range(1,3):
        new_df = df.sample(n=5)
        new_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\/' + str(i) + '_Deck.csv', index=False)

    print('cards have been shuffled and decks have been dealt!')

def usablestats():
    global HeaderList
    HeaderList = df.columns[4:-2].values.tolist()
    a = 1
    for i in HeaderList:
        print('Enter',(a),'For ',(i))
        a+=1

def statchoice():
    choice = input("Input help? (y/n): ")
    choice = choice.upper()
    val = False
    if choice == ('N'):
        val = True
    if choice == ('Y'):
        print("\nHere are the stats you can battle with!\n")
        usablestats()
        val = True
    elif val == False:
        print("\n!please answer (Y/N!)")
        statchoice()
        


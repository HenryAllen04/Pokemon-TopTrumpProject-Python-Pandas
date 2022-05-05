import numpy as np
import pandas as pd
import ShuffleStats as SS
import Battle as B
#Not adding types battles yet :)

def rounds():
    #this function begins the rounds
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    global AI_decksize
    global user_decksize

    
    user_deck_df = pd.read_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv')
    AI_deck_df = pd.read_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv')
    user_card = user_deck_df.sample()
    AI_card = AI_deck_df.sample()

    print("\n#YOUR CARD#\n")
    print(user_card.iloc[0].to_string(index=True)+'\n')
    


def HP_vs_HP():
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    
    print("\n#HP BATTLE#")
    print("----------------------------------------")
    print(user_card['Name'].to_string(index=False)," VS ",AI_card['Name'].to_string(index=False))
    print("HP:",user_card.iloc[0,4],"VS HP:",AI_card.iloc[0,4])
    print("----------------------------------------")
    if user_card.iloc[0,4] > AI_card.iloc[0,4]: # if hp on user card is greater
        
        #user card win
        print("#DECK UPDATE WIN#")
        print("----------------------------------------")
        print("New pokemon caught:",AI_card['Name'].to_string(index=False))

        user_deck_df = pd.concat((user_deck_df, AI_card), axis = 0) # this takes the AI's card and adds it to the users deck
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        AI_deck_df = pd.concat((AI_deck_df, AI_card), axis = 0).drop_duplicates(keep=False) # this takes the AI card duplicates it by adding it onto the AI deck then deletes all duplicates
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

    elif user_card.iloc[0,4] == AI_card.iloc[0,4]:
        print("#DECK UPDATE DRAW#")
        print("----------------------------------------")
        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")
    else:
        print("#DECK UPDATE LOSS#")
        print("----------------------------------------")
        print("Pokemon lost:",user_card['Name'].to_string(index=False))
       
        #AI card win
        AI_deck_df = pd.concat((AI_deck_df, user_card), axis = 0)
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        user_deck_df = pd.concat((user_deck_df, user_card), axis = 0).drop_duplicates(keep=False)
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")


def ATTACK_vs_ATTACK():
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    
    print("\n#ATTACK BATTLE#")
    print("----------------------------------------")
    print(user_card['Name'].to_string(index=False)," VS ",AI_card['Name'].to_string(index=False))
    print("ATTACK:",user_card.iloc[0,5],"VS ATTACK:",AI_card.iloc[0,5])
    print("----------------------------------------")
    if user_card.iloc[0,5] > AI_card.iloc[0,5]: # if hp on user card is greater
        
        #user card win
        print("#DECK UPDATE WIN#")
        print("----------------------------------------")
        print("New pokemon caught:",AI_card['Name'].to_string(index=False))

        user_deck_df = pd.concat((user_deck_df, AI_card), axis = 0) # this takes the AI's card and adds it to the users deck
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        AI_deck_df = pd.concat((AI_deck_df, AI_card), axis = 0).drop_duplicates(keep=False) # this takes the AI card duplicates it by adding it onto the AI deck then deletes all duplicates
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

    elif user_card.iloc[0,5] == AI_card.iloc[0,5]:
        print("#DECK UPDATE DRAW#")
        print("----------------------------------------")
        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")
    else:
        print("#DECK UPDATE LOSS#")
        print("----------------------------------------")
        print("Pokemon lost:",user_card['Name'].to_string(index=False))
       
        #AI card win
        AI_deck_df = pd.concat((AI_deck_df, user_card), axis = 0)
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        user_deck_df = pd.concat((user_deck_df, user_card), axis = 0).drop_duplicates(keep=False)
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

def DEFENSE_vs_DEFENSE():
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    
    print("\n#DEFENSE BATTLE#")
    print("----------------------------------------")
    print(user_card['Name'].to_string(index=False)," VS ",AI_card['Name'].to_string(index=False))
    print("DEFENSE:",user_card.iloc[0,6],"VS DEFENSE:",AI_card.iloc[0,6])
    print("----------------------------------------")
    if user_card.iloc[0,6] > AI_card.iloc[0,6]: # if hp on user card is greater
        
        #user card win
        print("#DECK UPDATE WIN#")
        print("----------------------------------------")
        print("New pokemon caught:",AI_card['Name'].to_string(index=False))

        user_deck_df = pd.concat((user_deck_df, AI_card), axis = 0) # this takes the AI's card and adds it to the users deck
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        AI_deck_df = pd.concat((AI_deck_df, AI_card), axis = 0).drop_duplicates(keep=False) # this takes the AI card duplicates it by adding it onto the AI deck then deletes all duplicates
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

    elif user_card.iloc[0,6] == AI_card.iloc[0,6]:
        print("#DECK UPDATE DRAW#")
        print("----------------------------------------")
        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")
    else:
        print("#DECK UPDATE LOSS#")
        print("----------------------------------------")
        print("Pokemon lost:",user_card['Name'].to_string(index=False))
       
        #AI card win
        AI_deck_df = pd.concat((AI_deck_df, user_card), axis = 0)
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        user_deck_df = pd.concat((user_deck_df, user_card), axis = 0).drop_duplicates(keep=False)
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

def SP_ATK_vs_SP_ATK():
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    
    print("\n#SP_ATK BATTLE#")
    print("----------------------------------------")
    print(user_card['Name'].to_string(index=False)," VS ",AI_card['Name'].to_string(index=False))
    print("SP_ATK:",user_card.iloc[0,7],"VS SP_ATK:",AI_card.iloc[0,7])
    print("----------------------------------------")
    if user_card.iloc[0,7] > AI_card.iloc[0,7]: # if hp on user card is greater
        
        #user card win
        print("#DECK UPDATE WIN#")
        print("----------------------------------------")
        print("New pokemon caught:",AI_card['Name'].to_string(index=False))

        user_deck_df = pd.concat((user_deck_df, AI_card), axis = 0) # this takes the AI's card and adds it to the users deck
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        AI_deck_df = pd.concat((AI_deck_df, AI_card), axis = 0).drop_duplicates(keep=False) # this takes the AI card duplicates it by adding it onto the AI deck then deletes all duplicates
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

    elif user_card.iloc[0,7] == AI_card.iloc[0,7]:
        print("#DECK UPDATE DRAW#")
        print("----------------------------------------")
        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")
    else:
        print("#DECK UPDATE LOSS#")
        print("----------------------------------------")
        print("Pokemon lost:",user_card['Name'].to_string(index=False))
       
        #AI card win
        AI_deck_df = pd.concat((AI_deck_df, user_card), axis = 0)
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        user_deck_df = pd.concat((user_deck_df, user_card), axis = 0).drop_duplicates(keep=False)
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

def SP_DEF_vs_SP_DEF():
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    
    print("\n#SP_DEF BATTLE#")
    print("----------------------------------------")
    print(user_card['Name'].to_string(index=False)," VS ",AI_card['Name'].to_string(index=False))
    print("SP_DEF:",user_card.iloc[0,8],"VS SP_DEF:",AI_card.iloc[0,8])
    print("----------------------------------------")
    if user_card.iloc[0,8] > AI_card.iloc[0,8]: # if hp on user card is greater
        
        #user card win
        print("#DECK UPDATE WIN#")
        print("----------------------------------------")
        print("New pokemon caught:",AI_card['Name'].to_string(index=False))

        user_deck_df = pd.concat((user_deck_df, AI_card), axis = 0) # this takes the AI's card and adds it to the users deck
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        AI_deck_df = pd.concat((AI_deck_df, AI_card), axis = 0).drop_duplicates(keep=False) # this takes the AI card duplicates it by adding it onto the AI deck then deletes all duplicates
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

    elif user_card.iloc[0,8] == AI_card.iloc[0,8]:
        print("#DECK UPDATE DRAW#")
        print("----------------------------------------")
        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")
    else:
        print("#DECK UPDATE LOSS#")
        print("----------------------------------------")
        print("Pokemon lost:",user_card['Name'].to_string(index=False))
       
        #AI card win
        AI_deck_df = pd.concat((AI_deck_df, user_card), axis = 0)
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        user_deck_df = pd.concat((user_deck_df, user_card), axis = 0).drop_duplicates(keep=False)
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

def SPEED_vs_SPEED():
    global AI_deck_df
    global user_deck_df
    global user_card
    global AI_card
    
    print("\n#SPEED BATTLE#")
    print("----------------------------------------")
    print(user_card['Name'].to_string(index=False)," VS ",AI_card['Name'].to_string(index=False))
    print("SPEED:",user_card.iloc[0,9],"VS SPEED:",AI_card.iloc[0,9])
    print("----------------------------------------")
    if user_card.iloc[0,9] > AI_card.iloc[0,9]: # if hp on user card is greater
        
        #user card win
        print("#DECK UPDATE WIN#")
        print("----------------------------------------")
        print("New pokemon caught:",AI_card['Name'].to_string(index=False))

        user_deck_df = pd.concat((user_deck_df, AI_card), axis = 0) # this takes the AI's card and adds it to the users deck
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        AI_deck_df = pd.concat((AI_deck_df, AI_card), axis = 0).drop_duplicates(keep=False) # this takes the AI card duplicates it by adding it onto the AI deck then deletes all duplicates
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

    elif user_card.iloc[0,9] == AI_card.iloc[0,9]:
        print("#DECK UPDATE DRAW#")
        print("----------------------------------------")
        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")
    else:
        print("#DECK UPDATE LOSS#")
        print("----------------------------------------")
        print("Pokemon lost:",user_card['Name'].to_string(index=False))
       
        #AI card win
        AI_deck_df = pd.concat((AI_deck_df, user_card), axis = 0)
        AI_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\2_Deck.csv', index=False)

        user_deck_df = pd.concat((user_deck_df, user_card), axis = 0).drop_duplicates(keep=False)
        user_deck_df.to_csv(r'C:\Users\20241779\OneDrive - Farnborough College of Technology\PandaPokemonTopTrumpProject\UserVsAIDecks\1_Deck.csv', index=False)

        print("Size of deck:",len(user_deck_df))
        print("----------------------------------------")

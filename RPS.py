'''
Rock , Paper , Scissor 

1 for Rock 
0 for Paper 
-1 for Scissor
'''
import random

# Dictionry for keys and value
choiceDict = {"rock": 1, "paper": 0, "scissor": -1}

# for scoring
scoreCom = 0
scoreyou = 0

# for Tracking Rounds Played
totalRound = 0

while True:
    # User input
    choice = input("Enter your choice (Rock/Paper/Scissor) or Q to quit: ").lower()
    if(choice == 'q'):
        print("Thanks For playing 😊")
        print(f"Total rounds played: {totalRound}")
        print(f"Final Score 🏅- You: {scoreyou}| Computer: {scoreCom} ")
        break
        
    if choice  not in choiceDict:
        print("Invalid choice ❌ , try again.")
        continue
    totalRound +=1
    # computer choosing random value
    comChoice= random.choice(list(choiceDict.keys()))
    comValue = choiceDict[comChoice]
    you = choiceDict[choice]
    print(f"Computer choose : {comChoice}")

    # Equal 
    if(comValue == you):
        print("It's a Tie!!") 

    # scissor < stone   : 1
    # paper < scissor  : -1
    # stone < paper    : 0  
    elif((comValue==-1 and you==1)or\
        (comValue==0 and you==-1)or\
        (comValue==1 and you==0)):
        print("You Win!🥳") 
        scoreyou +=1 
    else:     
        print("You lose!😓")
        scoreCom +=1        
    
    # Score Board
    print("-----Score Board-----")
    print(f"Computer💻:{scoreCom} | You 🥰:{scoreyou}")
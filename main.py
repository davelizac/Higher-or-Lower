from art import logo_1 
from art import logo_2
from game_data import data
from replit import clear
import random

#VARIABLES:
score = 0

#FUNCTIONS:
def selecting(a, b):
    """This function allows the users to type their selection"""
    more = input("\nWho has more followers? Type A or B: ").lower()
    return more
    

def compare(a, b):
    """This function shows the data from the contenders"""
    
    print(logo_1)

    print(f"\nYou're right! Your current score is: {score}")
    
    print(f"\nCompare 'A': {a['name']},  {a['description']}, from {a['country']}.")
    
    print(logo_2)
    
    print(f"'B': {b['name']}, {b['description']}, from {b['country']}.")
    
    
def contender():
    """This function selects random contenders from the stored data"""
    contender = data[random.randint(0, len(data) - 1)]
    return contender

#GAME STARTING POINT:

#Contenders selection:    
a = contender()

b = contender()

if a == b:
    b = contender()
    
#First match:
print(logo_1)

print(f"\nCompare 'A': {a['name']},  {a['description']}, from {a['country']}.")

print(logo_2)

print(f"'B': {b['name']},  {b['description']}, from {b['country']}.")


users_choice = selecting(a, b)

#Following matches:
run = True
while run:
    if users_choice == "a":
        users_choice = a
    elif users_choice == "b":
        users_choice = b        
    
    if users_choice == a and a["follower_count"] > b["follower_count"]:
        score += 1
        clear()
        a = a
        b = contender()
        if a == b:
            b = contender()
        compare(a, b)
        users_choice = selecting(a, b)
    elif users_choice == b and b["follower_count"] > a["follower_count"]:
        score += 1
        clear()
        a = b
        b = contender()
        if a == b:
            b = contender()
        compare(a, b)
        users_choice = selecting(a, b)
    else:
        run = False
        clear()
        print(logo_1)
        print("\nWrong answer!")
        print(f"your final score is {score}")
         
    
    
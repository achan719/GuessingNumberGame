## Guess The Number by codementor

# Write a programm where the computer randomly generates
# a number between 0 and 20. The user needs to guess what 
# the number is. If the user guesses wrong, tell them 
# their guess is either too high, or too low. This will 
# get you started with the random library if you haven't 
# already used it.


#%%
from random import randint

num = randint(1, 20)
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number: ")) 
    attempts += 1
    if guess == num:
        print("You've got it!")
        break
    elif guess < num:
        print ("You entered ", guess, "- that is too low")
    else: 
        print ("You entered ", guess, "- that is too high")
if guess == num: 
    print("Congrats")
else:
    print("You've reached the max limit. Try again")

# %%

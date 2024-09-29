import random

def start_game():
    num= random.randint(1,100)
    attempts= 0
    print("Welcome to the number guessing game!\nI am guessing number between 1 to 100.\n")
    
    level = input("Choose difficulty level! Enter 'Easy' or 'Hard'.\n")
    if str.lower(level) == 'easy':
        attempts= 10
        guess_num(attempts,num)
    elif str.lower(level) == 'hard':
        attempts= 5
        guess_num(attempts,num)
    else:
        print("!!!Please choose correct Level!!!\n")
        start_game()
    
def guess_num(attempts,num):
    
    if attempts !=0:
        guess= int(input(f"You have {attempts} attempts to guess the number!\nMake a guess:"))
        if guess < num:
            print("Too Low.\nGuess again!\n")
            guess_num(attempts -1, num)
        elif guess > num:
            print("Too High.\nGuess again!\n")
            guess_num(attempts -1, num)
        elif guess == num:
            print("Congratulations you WON!\n")
    elif attempts== 0:
        print("OOPS! you ran out of attempts please try again.")     
        start_game()
start_game()
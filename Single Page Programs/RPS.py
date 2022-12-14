import random

user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock, Paper, or Scissors or \"Q\" to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    #! Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    
    if user_input == computer_pick:
        print("It's a draw, go again!")
        draw += 1
        continue
    
    else:
        print("You lost, the pesky computer wins this one.")
        computer_wins += 1


#?Use Ternary Operator to change this up, as well as multiline string interpolation. Will come back to this.  
print()
print("You won", user_wins, "times.")
print()
print("The computer won", computer_wins, "times.")
print()
print(f"You and the computer came to a draw {draw} times.")    
print()
print("Goodbye!")
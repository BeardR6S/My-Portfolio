import random

top_range = input("Type a Number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print('Please type a number larger then 0 next time, thank you.')
        quit()
else:
    print('Please type a number next time, thank you.')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time, thank you.')
        continue

    if user_guess == random_number:
        print("Nicely done, you guessed correctly!")
        break
    elif user_guess > random_number:
            print(f"Your guess is higher then the number, try guessing a number that is below {user_guess}.")
    else:
            print(f"Your guess was lower then the number, try guessing a number that is higher than {user_guess}")

print("You guessed the number correctly in", guesses, "guesses!!!")
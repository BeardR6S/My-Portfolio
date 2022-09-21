print('Welcome to my program')

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()
    
print("Let's play the game!!!")
score = 0

#!Q1
answer = input("What programming language is this game written in? ")
if answer.lower() == "python":
    print('Correct! Nicely done.')
    score += 1
else: 
    print('Unfortunately that is incorrect. Don\'t give up though, You got this!!! ')

#!Q2
answer = input("What is 10 + 5? ")
if answer == "15":
    print('Correct!')
    score += 1
else: 
    print('Not quite, good try though, keep going!')

#!Q3
answer = input("What machine was Alan Turing famous for? ")
if answer.lower() == "turing machine":
    print('Amazing, you know your stuff! He used the "Turing Machine" to help crack the "Enigma Code" during World War Two.')
    score += 1
else: 
    print('Incorrect, He was known for the "Turing Machine". He helped crack the "Enigma code" during World War 2, using said machine! ')

#!Q4
answer = input("Is Javascript a programming language? ")
if answer.lower() == "yes":
    print('That is correct')
    score += 1
else: 
    print('Incorrect, It is a programming language.')

#!Q5
answer = input("What color is healthy grass?" )
if answer.lower() == "green":
    print('That is correct!')
    score += 1
else: 
    print('Incorrect.')

#!Q6
answer = input("Can you learn programming/coding on youtube? ")
if answer.lower() == "yes":
    print('That is correct')
    score += 1
else: 
    print('Incorrect.')

#!Q7
answer = input("What is the name/mascot of the NFL Football team in Charlotte, North Carolina? ")
if answer.lower() == "panthers":
    print('That is correct')
    score += 1
else: 
    print('Incorrect.')

#!Q8
answer = input("What is the name/mascot of the NFL Football team located in Cincinnati, Ohio? ")
if answer.lower() == "bengals":
    print('That is correct')
    score += 1
else: 
    print('Incorrect.')

print(f"You got {score} out of 8 questions correct.") 
print("You got " + str((score/8) * 100)+'% correct out of 100.0%.')
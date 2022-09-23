
#!Choose your own adventure game
name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You awake in a bed, you can either get up or go back to sleep. (get up/sleep): ").lower()

if answer == "sleep":
    answer = input("You chose to sleep through the day, therefor missing out on the days adventure, you lose.")

elif answer == "get up":
        answer = input("You chose to get out of bed, you can either eat breakfast while watching scrolling through TikTok, or take a shower first then eat breakfast. (eat/shower): ").lower()
    
if answer == "eat":
        print("You chose to eat first while scrolling through TikTok, however while doing so you lost track of time and end up just staying home all day. You lose the game.")
    
elif answer == "shower":
    answer = input("You decided to take your shower first then eat. After you finish eating you look at your phone and realize its time to head to work, do you walk or drive to work? (walk/drive): ").lower()
        

if answer == "drive":
    print("You decided to drive to work, however you hit rush hour and end up being an hour late for work. You lose.")
        
elif answer == "walk":
    answer = input("You decide to walk to work, you grab your keys and head out the door. While walking to work, you pass by a coffee shop, do you stop and get some coffee? (yes/no): ").lower()

    if answer == "no":
        answer = input("You show up to work, around lunch you are extremely tired and end up falling asleep at your desk. Your boss fires you, you have lost.")
    elif answer == "yes":
        answer = input("You walk into the coffee shop, you order your cup of coffee and all the sudden confetti starts falling from the ceiling. You just won free coffee for yourself and your office for the week. However you have to sign up with an email to receive the giveaway. Do you give them your email? (yes/no)").lower()


#? print("Invalid input, you lose.") Not finished, so this is commented out as to not give a false invalid input.

#! I will be adding to this as time goes, and way it is coded, its a never ending/changed program.
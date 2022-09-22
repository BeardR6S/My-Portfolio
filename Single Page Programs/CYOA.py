
#!Choose your own adventure game
name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

q1 = input("You awake in a bed, you can either get up or go back to sleep, type \"get up\" to get up and \"sleep\" to go back to sleep: ").lower()

if q1 == "sleep":
    q1 = input("You chose to sleep through the day, therefor missing out on the days adventure, you lose.")

if q1 == "get up":
    q1 = input("You chose to get out of bed, you can either eat breakfast while watching scrolling through TikTok, or take a shower first then eat breakfast. Type \"eat\" to eat first, or \"shower\" to take a shower first: ").lower()
        
    if q1 == "eat":
        print("You chose to eat first while scrolling through TikTok, however while doing so you lost track of time and end up just staying home all day. You lose the game.")
    
    elif q1 == "shower":
        print("You decided to take your shower first then eat, which gives you a refreshing start to your day.")
    
    else:
        print("Invalid input, you lose.")

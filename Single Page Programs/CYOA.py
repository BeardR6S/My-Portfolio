
#!Choose your own adventure game
name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You awake in a bed, you can either get up or go back to sleep, type \"get up\" to get up and \"sleep\" to go back to sleep: ").lower()

if answer == "sleep":
    answer = input("You chose to sleep through the day, therefor missing out on the days adventure, you lose.")

elif answer == "get up":
    answer = input("You chose to get out of bed, you can either eat breakfast while watching scrolling through TikTok, or take a shower first then eat breakfast. Type \"eat\" to eat first, or \"shower\" to take a shower first: ").lower()
        
    if answer == "eat":
        print("You chose to eat first while scrolling through TikTok, however while doing so you lost track of time and end up just staying home all day. You lose the game.")
    elif answer == "shower":
        print("You decided to take your shower first then eat. After you finish eating you look at your phone and realize its time to head to work, do you walk or drive to work? (walk/drive)")
        if answer == "walk":
            answer = input("You decide to walk to work, you grab your keys and head out the door. While walking to work, you pass by a coffee shop, do you stop and get some coffee? (yes/no): ")
        
    else:
        print("Invalid input, you lose.")
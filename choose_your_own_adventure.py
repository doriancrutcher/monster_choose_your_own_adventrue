import random

def play_game():
    print("Welcome to the haunted house, your mission is to avoid the monster and find a way out.")

    # Initialize game variables
    has_weapon = False
    monster_rooms = random.sample(['red', 'blue', 'yellow'], 2)  # Randomly place the monster in 2 out of 3 rooms
    weapon_room = list(set(['red', 'blue', 'yellow']) - set(monster_rooms))[0]  # The remaining room has the weapon

    print("You stand before three doors: Red, Blue, and Yellow.")
    while True:
        door = input("Which door do you choose? Red, Blue, or Yellow?\n").lower()
        
        if door in ['red', 'blue', 'yellow']:
            if door in monster_rooms:
                if has_weapon:
                    print(f"You encounter the monster in the {door} room!")
                    fight_or_flee = input("Do you want to fight or flee? (fight/flee)\n").lower()
                    if fight_or_flee == "fight":
                        print("You bravely fight the monster and win! You find the exit behind the monster. YOU WIN!!!")
                        return
                    elif fight_or_flee == "flee":
                        print("You narrowly escape back to the starting point.")
                    else:
                        print("Invalid choice, the monster gets you. GAME OVER.")
                        return
                else:
                    print(f"You encounter the monster in the {door} room and have no weapon to fight it. GAME OVER.")
                    return
            elif door == weapon_room:
                has_weapon = True
                print(f"You find a weapon in the {door} room! Now you can fight the monster.")
            else:
                print(f"The {door} room is empty, but you feel a cold breeze.")
        else:
            print("Invalid choice. Please choose a valid door: Red, Blue, or Yellow.")

# Start the game
play_game()

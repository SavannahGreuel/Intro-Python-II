from room import Room
from player import Player
from item import Item
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['matches', 'lamp', 'shoes', 'map']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['rope', 'pick axe', 'dog']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['wagon', 'rocks']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure! You're adventure has been victorious, for you have won the game! The only exit is to the south.""", ['hidden-treasure']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Hello there! What is your name?\n >>')
player = Player(name, room['outside'])

print(f'Welcome {name}, ready for our adventure?') 
print('-------------')
time.sleep(2)

print('The evil monkeys have stolen my hidden treasure, and i need your help to retrieve it') 
print('-------------')
time.sleep(2)

print('Navigate through the magical world of of narnia to find the treasure. Find the treasure to win the game') 
print('-------------')
time.sleep(2)

print("To Move: enter n to go north, e to go east, w to go west, and s to go south")
print('-------------')
time.sleep(3)
print("Instructions: enter q to quit, enter i or inventory to see whats in your inventory")
print('-------------')
time.sleep(3)
print("To see what items are in the room you are currently in, enter r")
print('-------------')
time.sleep(3)
print("To pick up an item that is in the room, enter 'get 'item name'' or 'take 'items name' ")
print('-------------')
time.sleep(3)
print("To drop an item that is in your inventory, enter 'drop 'item name''  ")
print('-------------')
time.sleep(3)
print("To see all these instructions again at any point during your adventure, enter x")
print('-------------')
time.sleep(3)
# Write a loop that:
#
# * Prints the current room name

while True:

    # * Prints the current description (the textwrap module might be useful here).
    print(f'You are located here: {player.room.name}')
    print(f'{player.room.description}')
    print('-------------')
    time.sleep(2)

    choice = input("'Enter Command'>> ").lower()

    choice = choice.split(" ")


    if (len(choice) == 1):
        if(choice[0] == "q"):
            print('\n See you next time!')
            time.sleep(1)
            quit()

        elif(choice[0] == 'x'):
            print("To Navigate: enter n to go north, e to go east, w to go west, and s to go south")
            print('-------------')
            time.sleep(3)
            print("Instructions: enter q to quit, enter i or inventory to see whats in your inventory")
            print('-------------')
            time.sleep(3)
            print("To see what items are in the room you are currently in, enter r")
            print('-------------')
            time.sleep(3)
            print("To pick up an item that is in the room, enter 'get 'item name'' or 'take 'items name' ")
            print('-------------')
            time.sleep(3)
            print("To drop an item that is in your inventory, enter 'drop 'item name''  ")
            print('-------------')
            time.sleep(3)
            print("To see all these instructions again at any point during your adventure, enter instructions ")
            print('-------------')
            time.sleep(3)

        elif(choice[0] == 'n'):
            try:
                time.sleep(1)
                player.room = player.room.n_to
            except AttributeError:
                print("Cannot move North, try a different direction")
                time.sleep(3)
        
        elif(choice[0] == 'e'):
            try:
                time.sleep(1)
                player.room = player.room.e_to
            except AttributeError:
                print("Cannot move East, try a different direction")
                time.sleep(3)   

        elif(choice[0] == 'w'):
            try:
                time.sleep(1)
                player.room = player.room.w_to
            except AttributeError:
                print("Cannot move West, try a different direction")
                time.sleep(3)    

        elif(choice[0] == 's'):
            try:
                time.sleep(1)
                player.room = player.room.s_to
            except AttributeError:
                print("Cannot move South, try a different direction")
                time.sleep(3) 

        elif(choice[0] == 'r'):
            if(player.room.items == []):
                print('There are no items in this room')
                time.sleep(3)
            else:
                print(f'Room contents: {player.room.items}')
                time.sleep(3)
                
        elif(choice[0] == 'i' or 'inventory'):
            if(player.inventory == []):
                print('You have nothing in your possession')
                time.sleep(3)
            elif (player.inventory.count('hidden-treasure') > 0):
                print('You have successfully completed the adventure! You Win....')
                break
            else:
                print(f'Your Possessions: {player.inventory}')
                time.sleep(3)
        
        else:
            time.sleep(1)
            print('Hmmm, looks like you gave an invalid command...try again')  
            print('-------------')          
            time.sleep(3)

    elif(len(choice) == 2):
        if(choice[0] == 'get' or choice[0] == 'take'):
            try:
                for i, item in enumerate(player.room.items):
                    if(item.name == choice[1]):
                        player.inventory.append(item.name)
                        player.room.items.remove(item)
                        print(f'You picked up a {choice[1]}')
                        time.sleep(3)
                        break
                    elif(i == len(player.room.items)-1):
                        print('There are no items for you to pick up here')
                        time.sleep(3)
                        break

            except AttributeError:
                for i, item in enumerate(player.room.items):
                    if (item == choice[1]):
                        player.inventory.append(item)
                        player.room.items.remove(item)
                        print(f'You picked up a {choice[1]}')
                        time.sleep(3)
                        break
                    elif(i == len(player.room.items)-1):
                        print('There are no items for you to pick up here')
                        time.sleep(3)
                        break

        elif(choice[0] == 'drop'):
            for i, item in enumerate(player.inventory):
                if(player.inventory[i] == choice[1]):
                    player.inventory.remove(item)
                    player.room.items.append(item)
                    print(f'You just dropped {choice[1]}')
                    time.sleep(3)
                elif(i == len(player.inventory)-1):
                    print(f'You have nothing in your inventory to drop')
                else:
                    print(f'There is nothing in your inventory named {choice[1]}')
                    time.sleep(3)
                    

        else:
            print(f'{choice[0]} is not a command')


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

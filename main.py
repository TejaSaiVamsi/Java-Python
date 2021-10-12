#MAJOR-PROJECT : TREASURE HUNT GAME
def lets_play_again() :
    print("\nDo you want to play again ? (y or n)")
    answer1 = input(">").lower()
    if answer1 =='y' :
        start()
    elif answer1 == 'n':
        exit()
def game_over() :
    print("\nGame over!!!")
def treasure_room() :
    print("\nYou are now in a room filled with diamonds")
    print("\nAnd there is a door too!")
    print("\nWhat would you do? (1 or 2)")
    print("\nTake some diamonds and go through the door")
    print("\nJust go through the door!")
    answer2 = input(">")
    print("\nYAYY!! YOU WIN!")

def monster_room() :
    print("\nNow you entered the room of a monster")
    print("\nThe monster  is sleeping now")
    print("\nBehind the monster there is another door")
    print("\nWhat would you do? (1 or 2)")
    print("\n1)Go through the door silently")
    print("\nKill the monster and show your courage!")
    answer3 = input(">")
    if answer3 == "1":
        treasure_room()
    elif answer3 == "2":
        print("\nThe monster is hungry, So the monster ate you!")
        game_over()

def snake_room():
    print("\nThere is a snake here..!")
    print("\nBehind the snake there is another door")
    print("\nThe snake is having eggs!!")
    print("\nWhat would you do? (1 or 2)")
    print("\n1)Take the eggs!")
    print("\n2)Taunt the snake.")
    answer4 = input(">")
    if answer4 == "1":
        print("\nYou want eggs not the treasure!! That's why the snake killed you!")
        game_over()
    elif answer4 == "2":
        treasure_room()

def start():
    print("\nYou are standing in a dark room!")
    print("\nThere is a door to  your left and right, Which one do you take? (l or r)")
    answer5 = input(">").lower()
    if answer5 == 'l':
        snake_room()
    elif answer5 == 'r' :
        monster_room()

start()
while 1:
    lets_play_again()

#PROJECT SUCCESSFULLY COMPLETED
#NAME : KANURI TEJA SAI VAMSI
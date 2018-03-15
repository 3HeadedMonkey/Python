from sys import exit, argv

script, name = argv


def welcome_function():
    print("""
    ###      ###
     ###    ###
      ########
       ######
        ####
        """)
    The_first_room()

def The_first_room():
    print("The first room, enter which door you wish to enter (1/2)")
    choice = input()

    if "1" in choice:
        The_second_room()
        welcome_function()
    elif choice == '2':
        The_third_room()
        welcome_function()
    elif choice =='exit':
        exit()
    else:
        print("Try again")
        The_first_room()

def The_second_room():
    print("\t You've entered the 2nd room, the loop game")
    print("how many loops do you wish to follow?")
    loop = input(">  ")
    loop = int(loop)
    loop_table = []

    for num in range(0, loop):
        numb = num+1
        print(f"Printing number {numb}")
        loop_table.append(num)

    print('\n', loop_table, '\n\n')
    return 0

def The_third_room():
    print("You've enetered the 3rd room, the teeths game")
    print("How may teeths you want me to print?")
    teeth = int(input('> '))
    print('How big should they be?')
    size = int(input('> '))
    for num in range(0, teeth):
        print('\n')
        Teeth_game(size)

def Teeth_game(num):
    dental = []
    for dent in range(0, num):
        dental.append('#')
        print(dental)
def exit():
    print("Goodbye")



print(f"Welcome {name}!, You've just started the Stupid Test Game, STG!")
welcome_function()

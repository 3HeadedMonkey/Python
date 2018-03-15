print(""" You enter a dark room with two dors.
Do you go though dorr #1 or door #2?""")

door = input("> ")

if door ==  "1":
    print("There is a enephant with a cheese for its head")
    print('What do you do?')
    print('1. Scream at the elepthant')
    print('2. Scream at the emendamer')

    elepthant = input('>>')

    if elepthant == '1':
        print("elepthant fagocitites you")
    elif elepthant == '2':
        print('elephant stomps you, gg')
    else:
        print('invalid choice, you die of shame')
elif door == "2":
    print("You've entered IKEA store")
    print("1. Go to the restaurant")
    print("2. Go to the door departament")
    print('3. People watching!')

    cox = input('I-K-E-A!~~')

    if cox == '1':
        print("Swedish kotbullen with rise and cramberry jam")
    elif cox == '2':
        print("You encounter Jehova Witness summer school, bravo, now you've joined the cult")
        input()
        print("ONE OF US, ONE OF US, ONE OF US")
    elif cox =='3':
        print('You\'ve encountered Crendor, you the two of you are peoplewatching')
    else:
        print("Something went wrond, you've been hired to IKEA?")

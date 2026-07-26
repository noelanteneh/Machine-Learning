print(r'''
*******************************************************************************
                     .---.
        .--.     ___/     \
       /    `.-""   `-,    ;
      ;     /     O O  \  /
      `.    \          /-'
     _  J-.__;      _.'
    (" /      `.   -=:
     `:         `, -=|
      |  F\    i, ; -|
      |  | |   ||  \_J

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the Elephant")

choose1 = input("You are in the middle of island. Do you want to go left or right? ").lower()

if choose1 == "right":
    choose2 = input("In front of you is a lake. Do you swim or wait for a boat? ").lower()

    if choose2 == "wait" or choose2 == "wait for a boat" or choose2== "boat":
        print("You're out of the island safe and unharmed!")

        choose3 = input("You are in the city. Take a bus or a taxi? ").lower()

        if choose3 == "taxi":
            print("You died in a car accident! Game Over.")
        elif choose3 == "bus":
            print("You're too late, the elephant got killed! Game Over.")
        else:
            print("You wrote a wrong option.")
    elif choose2 == "swim":
        print("you are attacked by angry sharks. Game Over.")
    else:
        print("You wrote a wrong option.")

elif choose1 == "left":
    choose2 = input("Enter the zoo by the door or jump over the fence? ").lower()
    if choose2 == "door":
        print("You got caught by the kidnappers! Game Over.")

    elif choose2 == "jump" or choose2 == "jump over the fence" or choose2 == "fence":
        choose3 = input("There are 3 doors in front of you: red, blue, or yellow. ").lower()

        if choose3 == "red":
            print("You entered a room filled with fire! Game Over.")
        elif choose3 == "blue":
            print("You entered a room filled with beasts! Game Over.")
        elif choose3 == "yellow":
            print("You saved the elephant! Excellent!")


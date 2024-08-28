def game():
    """
    Welcome message and start of game.
    Get name from user.
    """
    print("Welcome to a virtual hike.")
    print("We are going to hike 50km today.")
    print("Are you ready to hike?")
    print("But first, what is your name? ")
    name = input()
    capitalized_name = name.capitalize()
    print(f"Welcome, {capitalized_name}. Let's get ready to hike.\n")
    startingPoint()


def startingPoint():
    """
    First point where user has to make a right decission
    """
    print("I hope you brought everything you need for a hike.")
    print("Do you need a map of todays tour? y/n ")
    option = input()
    if option == "y":
        print("Great. Here is your map. Let's go to the first service point.\n")
        firstServicePoint()
    elif option == "n":
        print("Okay, no map for you. Let's start our hike.\n")
        meetFakeFriend()
    else:
        invalidChoice()
        startingPoint()


def invalidChoice():
    print("You entered an invalid option. Please try again.")

game()

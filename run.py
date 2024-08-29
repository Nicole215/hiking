import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def game():
    """
    Welcome message and start of game.
    Get name from user.
    """
    print("Welcome to a virtual hike.")
    print("We are going to hike 50km today.")
    print("Are you ready to hike?")
    print("You can quit any time by entering [q].")
    print(Fore.GREEN + "But first, what is your name? ")
    while True:
        name = input()
        capitalized_name = name.capitalize()
        if capitalized_name.isalpha():
            break
        else:
            print("Please enter only letters.")
    print(f"Welcome, {capitalized_name}. Let's get ready to hike.\n")
    startingPoint(capitalized_name)


def startingPoint(name):
    """
    First point where user has to make a right decission
    """
    print("I hope you brought everything you need for a hike.")
    print(Fore.GREEN + f"Do you need a map of todays tour, {name}? y/n ")
    try:
        option = input()
    except:
        print("Ups, something went wrong.")
    if option == "y":
        print("Here is your map. Let's go to the first service point.\n")
        firstServicePoint(name)
    elif option == "n":
        print("Okay, no map for you. Let's start our hike.\n")
        meetFakeFriend()
    elif option == "q":
        quit()
    else:
        invalidChoice()
        startingPoint(name)


def meetFakeFriend():
    """
    Game over part for wrong decission on starting point
    """
    print("Great, just 5km in you already made a new friend.")
    print("Unfortunatly your new friend is not part of our group.")
    print("Without a map you can't get back to the right path.")
    print(Fore.RED + "You are not taking part in our event anymore. Sorry.\n")
    game()


def firstServicePoint(name):
    """
    Second point where user has to make a right decission
    """
    print(f"Welcome {name} to the first service point.")
    print("Here we have a free drink for you.")
    print(Fore.GREEN + "What would you like to have? Water, coffee or energy? w/c/e ")
    try:
        option = input()
    except:
        print("Ups, something went wrong.")
    if option == "w":
        print("Good choice. Keep on hiking.\n")
        secondServicePoint(name)
    elif option == "c":
        print(Fore.RED + "That wasn't the best choice.")
        print("Now you need to return to start to poop.\n")
        startingPoint(name)
    elif option == "e":
        print(Fore.BLUE + "Whoah Speedy Gonzales, watch your heartrate!\n")
        thirdServicePoint(name)  # Energy let's user jump to third Service Point
    elif option == "q":
        quit()
    else:
        invalidChoice()
        firstServicePoint(name)


def secondServicePoint(name):
    """
    Third point where user has to make a right decission
    """
    print(f"Welcome to the second service point, {name}.")
    print("We're halfway through. Congratulations so far.")
    print("We have some bananas and waffles for you. Enjoy.")
    print("Unfortunately it's starting to rain.")
    print(Fore.GREEN + "What are you going to do? Wait or hike on? w/h ")
    try:
        option = input()
    except:
        print("Ups, something went wrong.")
    if option == "h":
        print("You are a true hiker. Rain is not gonna hold us back.")
        print("Behind the next corner, sunshine awaits us.\n")
        thirdServicePoint(name)
    elif option == "w":
        print("The rain lasts for hours. You give up. A bus takes you home.")
        print("Thank you for hiking with us.")
        print(Fore.RED + "Next time you'll make it to the finish line.\n")
        game()
    elif option == "q":
        quit()
    else:
        invalidChoice()
        secondServicePoint(name)


def thirdServicePoint(name):
    """
    Fourth point where user has to make a right decission
    """
    print("Welcome to the third service point. Almost there!")
    print("Let's have a little more to eat.")
    print(Fore.GREEN + "Do you want some fruit or just some water? f/w ")
    try:
        option = input()
    except:
        print("Ups, something went wrong.")
    if option == "f":
        print("Good choice. Those last kilometers will be hard.")
        print("But you can do it!\n")
        finishLine(name)
    elif option == "w":
        print("Oh no! You've come so far, but now you get cramps.")
        print(Fore.RED + "A bus will take you back home.")
        print(f"Thank you for hiking with us, {name}.")
        print("Next time you'll make it to the finish line.\n")
        game()
    elif option == "q":
        quit()
    else:
        invalidChoice()
        thirdServicePoint(name)


def finishLine(name):
    """
    End of game if all decissions by user were right
    """
    print(Fore.YELLOW + "Congratulations! You just hiked 50 kilometers!")
    print(f"Here is your finisher beer, {name}. Enjoy!")
    quit()


def invalidChoice():
    print("You entered an invalid option. Please try again.")


# Calling game function
if __name__ == "__main__":
    game()

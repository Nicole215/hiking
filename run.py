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


def meetFakeFriend():
    """
    Game over part for wrong decission on starting point
    """
    print("Great, just 5km in you already made a new friend.")
    print("Unfortunatly your new friend is not part of our group.")
    print("Without a map you can't get back to the right path.")
    print("You are not taking part in our event anymore. Sorry.\n")
    game()


def firstServicePoint():
    """
    Second point where user has to make a right decission
    """
    print("Welcome to the first service point.")
    print("Here we have a free drink for you.")
    print("What would you like to have? Water or coffee? w/c ")
    option = input()
    if option == "w":
        print("Good choice. Keep on hiking.\n")
        secondServicePoint()
    elif option == "c":
        print("That wasn't the best choice.")
        print("Now you need to return to start to poop.\n")
        startingPoint()
    else:
        invalidChoice()
        firstServicePoint()


def secondServicePoint():
    """
    Third point where user has to make a right decission
    """
    print("Welcome to the second service point.")
    print("We're halfway through. Congratulations so far.")
    print("We have some bananas and waffles for you. Enjoy.")
    print("Unfortunately it's starting to rain.")
    print("What are you going to do? Wait or hike on? w/h ")
    option = input()
    if option == "h":
        print("You are a true hiker. Rain is not gonna hold us back.")
        print("Behind the next corner, sunshine awaits us.\n")
        thirdServicePoint()
    elif option == "w":
        print("The rain lasts for hours. You give up. A bus takes you home.")
        print("Thank you for hiking with us.")
        print("Next time you'll make it to the finish line.\n")
        game()
    else:
        invalidChoice()
        secondServicePoint()


def thirdServicePoint():
    """
    Fourth point where user has to make a right decission
    """
    print("Welcome to the third service point. Almost there!")
    print("Let's have a little more to eat.")
    print("Do you want some more fruit or just some water? f/w ")
    option = input()
    if option == "f":
        print("Good choice. Those last kilometers will be hard.")
        print("But you can do it!\n")
        finishLine()
    elif option == "w":
        print("Oh no! You've come so far, but now you get cramps.")
        print("A bus will take you back home.")
        print("Thank you for hiking with us.")
        print("Next time you'll make it to the finish line.\n")
        game()
    else:
        invalidChoice()
        thirdServicePoint()


def finishLine():
    """
    End of game if all decissions by user were right
    """
    print("Congratulations! You just hiked 50 kilometers!")
    print("Here is your finisher beer. Enjoy!")
    quit()


def invalidChoice():
    print("You entered an invalid option. Please try again.")


# Calling game function
game()

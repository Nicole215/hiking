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

game()

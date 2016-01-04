def start():
    print("The police is chasing you.")
    print("You want to escape but you can't run as fast to shake them of.")
    print("You have to steal a car.")
    print("There is three cars: a german, a japanese and an american")
    print("Which one do you take")

    choice = input("> ")
    if "german" in choice:
        print("When you try to start up the car the car was blow up and you died.")
        exit(0)
    elif "american" in choice:
        print("After you start the car you are easily can shake of the cops"
              " but after five minutes you are run out of fuel and the police get you.")
        exit(0)
    elif "japanese" in choice:
        print("Because of the japanese cars reliability you can't even unlock it and the police get you.")
        exit(0)
    else:
        print("You can't decide which one to stole so you hide in the sewer and you luckily escape. Good job!")

start()
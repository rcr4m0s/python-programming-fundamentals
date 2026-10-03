lucky_number = 9
u = 0
guess_limit = 3

while u < guess_limit:
    nice = int(input("Guess: "))
    u += 1
    if nice == lucky_number:
        print("You won")
        break
    elif u == guess_limit:
        print("Sorry you've failed")




i = ""
started = False
while True:
    coms = input("> ").lower()
    if coms == "start":
        if started:
            print("The car already started")
        else:
            started = True
            print("The Car started")
    elif coms == "stop":
        print("The Car stopped")
    elif coms == "help":
        print("""
    start - to start the car
    stop - to stop the car
    quit - to quit
    """) 
    elif coms == "quit":
        break
    else:
        print("I don't understand that")
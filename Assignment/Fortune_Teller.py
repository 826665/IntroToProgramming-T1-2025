def Teller():

    print("Welcome, I am a Fortune teller you been seeking. I give you a number between 1-5 pick one.")
    input("Insert a number\n>")

    one = 1
    two = 2
    three = 3
    
    if one >= 1:
     print("Very Well, you picked card 1 which says.. How many years into the futrue do you wanna see?")
    input("How many years?")
    print("Very Well. Pick another card that isnt 1")

    if two >= 2:
        print("The card says.. If you could play any games early what would it be? ")
    input("What game?")
    print("Great Pick. Next number can't be 2")

    if three >= 3:
        print("What is your dream car?")
        input("Insert a car of your dreams")

    



Teller()
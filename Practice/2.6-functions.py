





# Parameters AND arguments print("you" * 5)
#Create a function that adds two numbers together
def add(x, y, z):
    print(x+y+z)

    
    add(10,30,20)
    add(12,4,28)




# Create a function called add_five numbers that takes five parameters
#-one for each number
#print the sum of the five numbers
#run the function three times with different arguments


def add_five_numbers(a, b, c, d, e):
    print(a + b + c + d + e)
    add_five_numbers(10, 20, 30, 40, 50)
    add_five_numbers(50,100.200,400,800)


def full_name(first, last):
    print(first + " " + last)
    
    first_name = input ("Enter your first name")
    Last_name = input ("Enter your last name")

    full_name(first_name, Last_name)

    def area_calculator(Length, Width):
        print(Length * Width)
    area_calculator(10,2)
    
    def word_smash(f, g):
        print(str(f) + str(g))

        word_smash("Cat, Dog")

        def echo(j, k):
            print( j * k)
        
        echo("you" * 5)

        def happy_birthday(name):
            print(name)
        
        
        Birthday_name = input ( "Insert a name for that birthday")
       
        
        
        happy_birthday("Happy Birthday To" + Birthday_name)
    
   

# String    - "in quitation"
#Integer    - "a whole number ex. 1 4 -10 etc."
#Float      - a decimal number ex. 3.1415435
#Char       - asingle glyph ex. "c"
#Bool       -True or Faluse

# How to define

lowercase = False
UPPERCASE = False
camelCase = False
UppercamelCase = False   #ALL lowercase, no spaces, capital for new words
LowercamelCase = False   #ALL lowercase, no spaces, capital for new words
snake_case = True        #All lowercase, underscores for space
SCREAMING_SNAKE_CASE = False


#Get the number as a string
number = input("What number do you want to square\n> ")


#Parse (Convert) the string to an integer (cast)

#Do math and print
number = int(number)
print(number * number)




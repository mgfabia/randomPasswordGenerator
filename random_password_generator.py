import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

digets = "0123456789"
symbols = "!@#$%^&*()-+"
password = ""

while True:
    var = input("Create password (or done)?")
    
    if (var == "y" or var == "yes" or var == "sure"):

        

        letter = int(input("How many letters?"))
        numbers = int(input("How many numbers?"))
        symb = int(input("How many special characters?"))
        length = letter + numbers + symb

        letrs = random.choices(letters,k = letter)
        num = random.choices(digets,k = numbers)
        special = random.choices(symbols,k = symb)
        #print(letrs)
        #print(num)
        #print(special)

        
        password = letrs + num + special
        random.shuffle(password)
        
        print("Your password is: " + "".join(password))
        
    elif (var == "done"):
        print("exiting program")
        break;
    else:
        print(var + " is not a valid input")

    

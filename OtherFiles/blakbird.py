
# now this is REALLY old code, most of this is copied from the internet
# coded by lewin pre-2018

import urllib.request
import time
import random
import string
from random import randint

print("BlakBird Allium v1.1.0. Booting Up.\n\nCopyright © VenimueCelestia Technologies Incorporated. All rights reserved.")

while True:
    username = input("\nWelcome to BlakBird! Please type your username:\n\n")

    username1 = "Lewin"
    username2 = "Username"
    
    if username == username1:
        print ("\nWelcome back, Creator! Please enter your password.")
        break
    elif username == username2:
        print ("\nHi there! Please enter your password.")
        break
    else:
        print ("\nThere is no user with this name. Try with caps?")
        
while True:
    password = input("\nPassword:\n\n")
        
    password1 = "Access"
    password2 = "Password"

    if password == password1 and username == username1:
        print ("\nHi there, Lewin!")
        break
    elif password == password2 and username == username2:
        print ("\nWelcome to the system, Epic!")
        break
    else:
        print ("\nAccess denied. All passwords are case-sensitive.")
        
print("Choices:\n \nShut down\nPrint notes\nInternet (ALPHA)\nDice Roll\nCalculator\n\nGAMES:\nPlay FizzBuzz\nMagic 8 ball\nGuess The Number\nComputer Quiz\nText Evolution\nHangman\nEscape the Cavern\nDroids")

while True:
    choice = input("\nWhat do you want to do?\n\n")

    if choice == "shut down" or choice == "shutdown":
        print("Shutting Down.")
        break

    elif choice == "print notes" or choice == "notes":
        if username == username1:
            print("\nHello\nThese are notes\nSub to pewdiepie\nNotes are cool\nthis operating system is cool\n\nTo Do:\nStop the system from crashing whenever I type a non-number into the quiz/calculator\n\nbye")
        else:
            print("\nEPIC EPIC EPIX SPACESHIPPPPPPPPPPPPPPPPPPPPPPPPPPPZZZZ R COOL HOW BOUT U")
    elif choice == "play fizzbuzz" or choice == "fizzbuzz":
        print('FizzBuzz is a game where you replace the multiples of three with "Fizz", the multiples of five with "Buzz" and the multiples of both with "FizzBuzz."\n')
        for i in range(1,101): print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i, end='\n')

    elif choice == "magic 8 ball" or choice == "8 ball":
        while True:
            question = input("Ask the Magic 8 ball a question: (Press enter to quit.) ")
            answers = random.randint(1,8)
            if question == "":
                break
            elif answers == 1:
                print("It is certain")
            elif answers == 2:
                print ("Outlook good")
            elif answers == 3:
                print ("You may rely on it")
            elif answers == 4:
                print ("Ask again later")
            elif answers == 5:
                print ("Concentrate and ask again")
            elif answers == 6:
                print ("Reply hazy, try again")
            elif answers == 7:
                print ("My reply is no")
            elif answers == 8:
                print ("My sources say no")
                
    elif choice == "internet" or choice == "net":
        webUrl  = urllib.request.urlopen('https://www.aol.co.uk/')
        print ("result code: " + str(webUrl.getcode()))
        data = webUrl.read()
        print (data)
        
    elif choice == "guess the number":
        n = random.randint(1, 99)
        guess = int(input("Enter an integer from 1 to 99: "))
        while n != "guess":
            print
            if guess < n:
                print("Higher!")
                guess = int(input("Enter an integer from 1 to 99: "))
            elif guess > n:
                print("Lower!")
                guess = int(input("Enter an integer from 1 to 99: "))
            else:
                print("you guessed it!")
                break
            
    elif choice == "dice roll" or choice == "dice":
        min = 1
        max = 6
        roll_again = "yes"
        while roll_again == "yes" or roll_again == "y":
            print("Rolling the dices...")
            print("The values are....")
            print(random.randint(min, max))
            print(random.randint(min, max))
            roll_again = input("Roll the dices again? Yes or no?\n\n")
            
    elif choice == "computer quiz" or choice == "quiz":
        my_dict =   {
                        "Base-2 number system" : "binary",
                        "Number system that uses the characters 0-F" : "hexidecimal",
                        "7-bit text encoding standard" : "ascii",
                        "16-bit text encoding standard" : "unicode",
                        "A number that is bigger than the maximum number that can be stored" : "overflow",
                        "8 bits" : "byte",
                        "1024 bytes" : "kilobyte",
                        "Picture Element. The smallest component of a bitmapped image" : "pixel",
                        "A continuously changing wave, such as natural sound" : "analogue",
                        "the number of times per second that a wave is measured" : "sample rate",
                        "A binary representation of a program" : "machine code"
                    }
        print("Welcome to... The computer Quiz!!!")
        print("==================================")
        playing = True
        while playing == True:
            score = 0
            num = int(input("\nHow many questions would you like?\n\n"))
            for i in range(num):
                question = (random.choice( list(my_dict.keys())))
                answer = my_dict[question]
                print("\nQuestion " + str(i+1) )
                print(question  + "?")
                guess = input("> ")
                if guess.lower() == answer.lower():
                    print("Correct!")
                    score += 1
                else:
                    print("Nope!") 
            print("\nYour final score was " + str(score))
            again = input("Enter any key to play again, or 'q' to quit.\n\n")
            if again.lower() == 'q':
                playing = False
                
    elif choice == "text evolution" or choice == "text":
        possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
        target = input("Enter your target text: ")
        attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
        attemptNext = ''
        completed = False
        generation = 0
        while completed == False:
            print(attemptThis)
            attemptNext = ''
            completed = True
            for i in range(len(target)):
                if attemptThis[i] != target[i]:
                    completed = False
                    attemptNext += random.choice(possibleCharacters)
                else:
                    attemptNext += target[i]
            generation += 1
            attemptThis = attemptNext
            time.sleep(0.035)
        print("Target matched! That took " + str(generation) + " generations!")
        
    elif choice == "calculator" or choice == "calc":
        print("1. Addition");
        print("2. Subtraction");
        print("3. Multiplication");
        print("4. Division");
        print("5. Exit");
        choice = int(input("Enter your choice: "));
        if (choice>=1 and choice<=4):
            print("Enter two numbers: ");
            num1 = int(input());
            num2 = int(input());
            if choice == 1:
                res = num1 + num2;
                print("Result = ", res);
            elif choice == 2:
                res = num1 - num2;
                print("Result = ", res);
            elif choice == 3:
                res = num1 * num2;
                print("Result = ", res);
            else:
                res = num1 / num2;
                print("Result = ", res);
        elif choice == 5:
            exit();
        else:
            print("Invalid input.");
            
    elif choice == "hangman":
        import random
        import time
        from time import sleep

        nesne="HANGMAN"
        simge="-"*50
        bos=""*5
        bilgi="""            You will earn 50 points if you guess a character correctly
                    and you will lose 25 points if your answer is wrong.
                    If you give 5 wrong answers you will lose."""
        print("{:^80}\n{:^80}\n{:^80}\n{:^80}\n{}".format(nesne,by,date,simge,bos))
        print(bilgi)
        print("{:^80}\n{:^80}\n{:^80}".format(bos,simge,bos))

        kelimeler = ["ability","about","above","absolute","accessible","accommodation",
                     "accounting","beautiful","bookstore","calculator","clever","engaged",
                     "engineer","enough","handsome","refrigerator","opposite","socks",
                     "interested","strawberry","backgammon","anniversary","confused",
                     "dangerous","entertainment","exhausted","impossible","overweight",
                     "temperature","vacation","scissors","accommodation","appointment",
                     "decrease","development","earthquake","environment","brand",
                     "environment","necessary","luggage","responsible","ambassador",
                     "circumstance","congratulate","frequent",]
        secim = random.choice(kelimeler)
        tablov=[]
        tablov.append("-"*len(secim))
        tablo=[]
        for i in tablov:
            for h in i:
                tablo.append(h)
        print("Our word has {} letters.".format(len(secim)),' '.join(tablo))
        print(""*7)
        c="""  _________
          |
          |"""
        c1="\n  O"
        c2="\n \|/"
        c3="\n  |"        
        c4="\n / \ "
        cson=""
        depo=""
        depo1=""
        a=len(depo)
        can=5
        puan=0
        olmazlar="+/ 1234567890*-_?.,"
        while True:
            if len(depo)==len(secim): 
                print("You won! Word: {} Your score: {}".format(secim,puan))
                print("Please press 'Enter' for quit..")
                break
            if can==0:
                print("\nYou lose...")
                sleep(0.9)
                print ("Your score: {}".format(puan))
                sleep(0.9)
                print ("The word that you couldnt answer: {}".format(secim))
                sleep(0.9)
                print("Please press 'Enter' for quit..")
                break

            x=input("\nPlease enter a letter: ")
            if 1<len(x):
                print ("\nYou can only enter 1 letter at a time.")
                continue
            if x in olmazlar:
                print("\nThis is not even a letter!")
                continue
            if x in depo:
                print("You have used this letter before!")
                continue
            if x in depo1:
                print("You have used this letter before!")
                continue
            if x in secim and not x in depo:
                puan+=50*secim.count(x)
                print("Letter {} is found {} times in our word!")
                #".format(x,secim.count(x)))
                sleep(0.7)
                for sayi, oge in enumerate(secim):
                    if 2 <=secim.count(oge) and x==oge:
                        depo+=x
                        a+=secim.count(oge)
                        if tablo[sayi]=="-": 
                            tablo[sayi]=x
                        print("In line {} .".format(sayi+1))
                        sleep(0.7)
                    if secim.count(oge)==1 and x==oge:
                        depo+=x
                        a+=secim.count(oge)
                        if tablo[sayi]=="-":
                            tablo[sayi]=x
                        print("In line {} .".format(sayi+1))
                        sleep(0.7)
                print("\nWord:",' '.join(tablo))
                sleep(0.7)

            else:
                depo1+=x
                can-=1
                puan-=25
                print("\nThis letter {} not in our word! {} guesses left.".format(x,can))
                sleep(0.7)
                print("\nWord:",' '.join(tablo))
                sleep(0.7)
                if can==4:
                    cson+=str(c)
                    print(cson)
                if can==3:
                    cson+=str(c1)
                    print(cson)      
                if can==2:          
                    cson+=str(c2)
                    print(cson)
                if can==1:
                    cson+=str(c3)
                    print(cson)
                if can==0:
                    cson+=str(c4)
                    print(cson)
        try:
            input()
        except SyntaxError:
            pass


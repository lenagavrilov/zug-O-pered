
def number():
    num = input("Enter your number:")
    if num.isdigit():
        print('Your number is: ' + str(num))
        return int(num)
    else:
        print (num + " is not a number")
        print("No number - no game! We'll start over!")
        players(zug_or_pered(text), number(), random())
        #number()
        #אם אני נכנסת לelse, אז כאשר כן בוחרים מספר vתוכנה עושה שגיאה

text = ""
def zug_or_pered(text):
    text = input('ZUG OR PERED?')
    if text == "zug" or text == "pered":
        print('Your choice is: ' + text)
        return str(text)
    else:
        print ("You can type'zug' or 'pered' only. Lets try again")
        players(zug_or_pered(text),number(),random())

from random import *
def random ():
    comp = randint(1,100)
    print("Comp chose number: "+ str(comp))
    return comp

def zugi_or_no(num, comp):   #3
    sum = num + comp
    print ('The sum is: '+ str(sum))
    if sum%2==0:
        print ("ZUGI!")
        #print (True)
        return True
    else:
        print ("I_ZUGI!")
       # print(False)
        return False

def players (text,num,comp):
    players = {}
    if text == 'zug':
        players.update({'zug': num})
        players.update({"pered": comp})
        print (players)
    else:
        if text == "pered":
            players.update({'pered':num})
            players.update({"zug": comp})
            print (players)

    x = zugi_or_no(num, comp)
    for each in players.keys():
        if (each == 'zug' and x == True) or (each == 'pered' and x== False):
            for value in players.values():
                if value == num:
                    print('You won!')
                    break
                else:
                    print('Computer won')
                    break
                break
            break

        else:
            if (each == 'pered' and x == True) or (each == 'zug' and x== False):
                for value in players.values():
                    if value == num:
                        print('Computer won!')
                        break
                    else:
                        print('You won')
                        break
                    break
                break
    another_game()

def another_game():
    while True:
        another_game = input('Press enter for another game. Press "stop" to finish')
        if another_game == 'stop':
            print ("We're done for now. See you soon")
            exit(0)
        players(zug_or_pered(text), number(), random())

players(zug_or_pered(text),number(),random())












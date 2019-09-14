
def number():
    num = input("Enter your number:")
    if num.isdigit():
        print('Your number is: ' + str(num))
        return int(num)
    else:
        print (num + " is not a number")
        print("No number - no game! We'll start over!")
        result(zug_or_pered(text), number(), random())
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
        result(zug_or_pered(text),number(),random())

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
    if text == 'zug':
        do_if_zug(text,num,comp)
    else:
        do_if_pered(text,num,comp)

def do_if_zug(text,num,comp):
    players = {}
    players.update({'zug': num})
    players.update({"pered": comp})
    print(players)
    who_is_who(text)
    return players

def do_if_pered(text,num,comp):
    players = {}
    players.update({'pered': num})
    players.update({"zug": comp})
    who_is_who(text)
    print(players)
    return players

def who_is_who(text):
    who_is_who = {}
    if text == 'zug':
        who_is_who.update({'player': 'zug'})
        who_is_who.update({'comp': 'pered'})
    else:
        who_is_who.update({'player': 'pered'})
        who_is_who.update({'comp': 'zug'})
    print(who_is_who)
    return who_is_who


def result(text,num,comp):
    sum_is_zugi = zugi_or_no(num,comp)
    #print(sum_is_zugi)
    if sum_is_zugi == True and who_is_who(text)['player']=='zug' or \
       sum_is_zugi == False and who_is_who(text)['player']=='pered':
        print('You won!')
    else:
        print('You lose!')
    another_game()

def another_game():
    while True:
        another_game = input('Press enter for another game. Press "stop" to finish')
        if another_game == 'stop':
            print ("We're done for now. See you soon :)")
            exit(0)
        result(zug_or_pered(text), number(), random())

#players(zug_or_pered(text),number(),random())
result(zug_or_pered(text),number(),random())












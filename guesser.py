import random
import easygui
tries = 0
number = random.randint(1, 100)
awnser = easygui.integerbox("Number between 1 and 100, what's your guess?")

while int(awnser) != number:
    tries = tries + 1
    if int(awnser) > number:
        easygui.msgbox("Too high, try again")
        awnser = easygui.integerbox("Awnser:")
    elif int(awnser) < number:
        easygui.msgbox("Too low, try again")
        awnser = easygui.integerbox("Awnser:")
tries = tries + 1
easygui.msgbox("Correct!, you had " + str(tries) + " tries")
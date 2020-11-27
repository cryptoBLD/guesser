import random
import easygui
tries = 0
guesses = 6
number = random.randint(1, 100)
awnser = easygui.integerbox("Number between 1 and 100, what's your guess?")

while int(awnser) != number and guesses != 0:
    tries = tries + 1
    if int(awnser) > number:
        easygui.msgbox("Too high, try again")
        awnser = easygui.integerbox("Awnser:")
        guesses -= 1
    elif int(awnser) < number:
        easygui.msgbox("Too low, try again")
        awnser = easygui.integerbox("Awnser:")
        guesses -= 1
tries = tries + 1
if guesses != 0:
    easygui.msgbox("Correct!, you had " + str(tries) + " tries")
else:
    easygui.msgbox("You failed idiot, the awnser was " + str(number))

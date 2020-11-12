"""
This is a multiplication game. If the player gets 10 points the player wins. Correct answer gives one point
and wrong answer drops points to zero. Printouts are in finnish.

"""
import random
import sys

print("Tervetuloa pelaamaan kertolaskupeliä. Saat yhden pisteen oikeasta vastauksesta. Väärästä tiput nollille.")
print("Voitat, jos saat 10 pistettä. Kirjoita 'lopeta', jos haluat lopettaa kesken.")

# The multiplication tables to be used in the game are given in this list
mt_list = [2, 5, 10]
points = 0
while points < 10:
    print("Sinulla on", points, "pistettä.")
    mt = random.choice(mt_list)

    # Multiplier is between 0 and 10
    multiplier = random.randint(0, 10)

    # The calculation string shown to the user
    calculation = "{} * {} = ".format(multiplier, mt)
    number = input(calculation)
    correct_answer = mt * multiplier

    # While loop is continued until the correct answer is given or the user wants to quit
    while True:
        if number == "lopeta":
            # If user wants to quit the game
            print("Kiitos pelaamisesta. Sait", points, "pistettä.")
            sys.exit()
        elif not number.isnumeric():
            # If given character is not a number
            print(number, "ei ole luku", end="\r\n")
            number = input(calculation)
        elif int(number) != correct_answer:
            # If given number is not correct the user is asked to try the same calculation again
            points = 0
            print("Väärin, sinulla on 0 pistettä. Yritä samaa laskua uudelleen", end="\r\n")
            number = input(calculation)
        else:
            # The correct answer breaks the loop
            break
    print("Oikein!")
    points += 1

print("Voitit, sait 10 pistettä. Kiitos pelistä.")

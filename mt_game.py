"""
This is a multiplication game. If the player gets 10 points the player wins. Correct answer gives one point
and wrong answer drops points to zero. There's 10 seconds to answer, exceeding that gives -1 point. Printouts are in finnish.

"""
import random
import sys
from inputimeout import inputimeout, TimeoutOccurred


# Function which fetches answer and checks if timeout occurs
def get_input_with_timeout(prompt, points):
    no_timeout = False
    response = ''
    while not no_timeout:
        no_timeout = True
        try:
            response = inputimeout(prompt=prompt, timeout=10)
        except TimeoutOccurred:
            no_timeout = False
            if points > 0:
                points -= 1
            print("Et antanut vastausta ajoissa. Sinulla on", points, "pistettä")
    return response, points


print("Tervetuloa pelaamaan kertolaskupeliä. Saat yhden pisteen oikeasta vastauksesta. Väärästä tiput nollille.")
print("Aikaa vastaukseen on 10 sekuntia, muuten vähennetään yksi piste.")
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
    number, points = get_input_with_timeout(calculation, points)
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
            number, points = get_input_with_timeout(calculation, points)
        elif int(number) != correct_answer:
            # If given number is not correct the user is asked to try the same calculation again
            points = 0
            print("Väärin, sinulla on 0 pistettä. Yritä samaa laskua uudelleen", end="\r\n")
            number, points = get_input_with_timeout(calculation, points)
        else:
            # The correct answer breaks the loop
            break
    print("Oikein!")
    points += 1

print("Voitit, sait 10 pistettä. Kiitos pelistä.")

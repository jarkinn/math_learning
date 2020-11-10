import random
import sys

print("Tervetuloa pelaamaan kertolaskupeliä. Saat yhden pisteen oikeasta vastauksesta. Väärästä tiput nollille.")
print("Voitat, jos saat 10 pistettä. Kirjoita 'lopeta', jos haluat lopettaa kesken.")
mt_list = [2, 5, 10]
points = 0
while True:
    mt = random.choice(mt_list)
    multiplier = random.randint(0, 10)
    calculation = "{} * {} = ".format(multiplier, mt)
    number = input(calculation)
    correct_answer = mt * multiplier
    while True:
        if number == "lopeta":
            print("Kiitos pelaamisesta. Sait", points, "pistettä.")
            sys.exit()
        elif not number.isnumeric():
            print(number, "ei ole luku", end="\r\n")
            number = input(calculation)
        elif int(number) != correct_answer:
            points = 0
            print("Väärin, sinulla on 0 pistettä. Yritä samaa laskua uudelleen", end="\r\n")
            number = input(calculation)
        else:
            break
    print("Oikein!")
    points += 1
    if points == 10:
        print("Voitit, sait 10 pistettä. Kiitos pelistä.")
        sys.exit()
    else:
        print("Sinulla on", points, "pistettä.")

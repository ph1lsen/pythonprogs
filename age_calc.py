# Character Input Practice https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input("Wie ist dein Name? ")
age = int(input("Wie alt bist du? "))
rando_num = int(input("Gib mir bitte noch eine zufällige Zahl zwischen 1 und 10 "))

def age_calc():
    current_year = 2024
    till_hundo = 100 - age
    calc_year = current_year + till_hundo
    random_num = rando_num
    while random_num > 0:
        print(f"Hey {name}! Im Jahr {calc_year} wirst du 100 Jahre alt sein!")
        random_num -= 1

age_calc()
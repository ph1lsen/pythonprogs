#Odd or Even Practice https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

num = float(input("Bitte gib mir eine Zahl: "))
check = float(input("Bitte gib mir eine weitere Zahl: "))

if num % 4 == 0:
    print(f"{num} ist ein vielfaches von vier")
elif num % 2 == 0:
    print(f"{num} ist eine runde Zahl")
else:
    print(f"{num} ist keine runde Zahl")


if num % check == 0:
    print(f"{num} durch {check} geht glatt auf.")
else:
    print(f"{num} geteilt durch {check} ist gleich {num / check}")

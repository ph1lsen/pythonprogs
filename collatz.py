def collatz(number):
    if number % 2 == 0:
        val = number//2
        print(val)
        return val
    elif number % 2 == 1:
        val = 3*number+1
        print (val)
        return val

def sequence():
    try:
        num = int(input("Give me a number: "))
        while num != 1:
            num = collatz(num)
    except ValueError:
        print("Please enter a Number.")


sequence()
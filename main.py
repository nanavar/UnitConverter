print("Hello there! I'm a unit converter, I'll help you convert kilometers to miles.")

while True:
    km = float(input("Enter the amount of kilometers: "))
    print(km * 0.621, "miles")

    choice = input("Do you want to do another conversion? (y/n): ")
    if choice.lower() != "y" and choice.lower() != "Y":
        break

print("Okay, bye-bye!")
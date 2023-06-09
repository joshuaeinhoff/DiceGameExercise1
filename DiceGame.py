import random

print("What is your name?")
name = input()
print("Hello, "+name+"!")
print("Rolling dice...")
dice1 = random.randint(1, 6)
print("Die 1: " + str(dice1))
dice2 = random.randint(1, 6)
print("Die 2: " + str(dice2))
totalValue = dice1 + dice2
print("Total value: " + str(totalValue))

if totalValue > 7:
    print(name + " won.")
else:
    print(name + " lost.")

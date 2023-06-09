import random

print("Rolling dice...")
dice1 = random.randint(1, 6)
print("Die 1: " + str(dice1))
dice2 = random.randint(1, 6)
print("Die 2: " + str(dice2))
totalValue = dice1 + dice2
print("Total value: " + str(totalValue))

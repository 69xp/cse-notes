import random

money_left = 15

while money_left != 0:
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    print(dice1,dice2)

    if dice1+dice2 == 7:
        money_left += 4
    else:
        money_left -= 1
    print("It took you %s turns to run out of moneys. Congrats you're broke!" )
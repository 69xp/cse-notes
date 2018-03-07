import random

money_left = 15

turns = 0

money_height = 0

best_turn = 0

while money_left != 0:
    if money_height < money_left:
        money_height = money_left
        best_turn = turns
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    print(dice1,dice2)

    if dice1+dice2 == 7:
        money_left += 4
        turns += 1
    else:
        money_left -= 1
        turns += 1
print("It took you %s turns to run out of moneys." % turns)
print("On turn %s you had the most moneys(%s)." % (best_turn, money_height))
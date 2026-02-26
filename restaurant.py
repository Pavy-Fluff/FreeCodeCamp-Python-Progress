# FreeCodeCamp - Python Basics
# How to write a moment where you are in a restaurant with your friends.

current_total = 0
friends = 3

mashed_potatoes = 30.29
caviar = 87.69
water = 3.99
steak = 55.99

cost = mashed_potatoes + caviar + water + steak
print("The total is:", round(cost, 2))

current_total += cost

tip = cost * 0.20

print("We gave the waiter a bonus, which was:", round(tip, 2))

current_total += tip
print('We "wasted" around', round(current_total, 2))

each_friend_pays = current_total / friends

print("Lets makes some fairness dude, we all pay", round(each_friend_pays, 2))
print("End")
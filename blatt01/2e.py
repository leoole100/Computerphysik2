#!/usr/bin/env python3

##
# @file 2e.py
# @brief find how many coins it takes on average so the sum is 1 ... 99 cents

coins = [50,20,10,5,2,1]

# r = remaining cost, m = max coin value
def coin_iteration(r,m):
    if r==0:
        return [0,1]
    coin_count = 0
    combinations = 0
    max_coins = 0
    for coin in coins:
        if (coin <= m) & (r >= coin):
            results = coin_iteration(r-coin,coin)
            coin_count += results[0] + 1 # each combination adds a certain amount of coins to the total, plus the one that was added in this iteration
            combinations += results[1]
    return [coin_count, combinations]
          

# find average coin count to sum up to 1 ... 99 cents => total coin count / combinations
print("Average coin count for a given total:\n")

for i in range(1,100):
    results = coin_iteration(i,50)
    print("\nSum: %d cents.\n   Combinations: %d\n   Coin Count: %d\n   Average Coin Count: %f\n" % (i,results[1],results[0],results[0]/results[1]))


print("\nHave a nice day!")

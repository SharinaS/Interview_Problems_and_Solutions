'''from Udemy's Python for data structures, Algorithms and Interviews

Problem: "Coin Change problem"
aka "knapsack type problem"
More info also available at https://en.wikipedia.org/wiki/Change-making_problem
And at http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html

Given a target amount n and a list / array of distinct coin values, what's the fewest coins needed to make the change amount?

Example:
n = 10
coins = [1, 5, 10]
4 solutions to make change:
1. 1+1+1+1+1+1+1+1+1+1
2. 5+1+1+1+1+1
3. 5+5
4. 10
'''

# Recursive solution that takes in target and coin list. Output the number of coins. Hint - use dynamic programming / memoization.

# RECURSIVE WITH DYNAMIC PROGRAMMING
# The function remembers past results, that way before computing a new minimum, we can check to see if we already know a result. The function takes in a target amount and a list of possible coins to use. It also takes in a third parameter, known_results, indicating previously calculated results. The known_results parameter should be started with [0] * (target+1)

def coin_dynamic(target, coins, known_results=None):
    if known_results == None:
        known_results = [0] * (target + 1)

    # default output to target
    min_coins = target

    # base case
    if target in coins:
        known_results[target] = 1

    # return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
            return known_results[target]

    else:
        # for every coin value that is <= target
        for i in [c for c in coins if c <= target]:
            #This for loop tests all the possible permutations starting with each coin (1, 5, 10, and 25), so one combination starting with a penny, then for the nickel and so forth. that would sum up to the target. Then it returns the length of the combination with the lowest number.
            num_coins = 1 + coin_dynamic(target-i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins

                # reset that known result
                known_results[target] = min_coins

    return min_coins

print(coin_dynamic(74, [1, 5, 10, 25]))


# My pseudocode for an iterative solution (postnote - iteration in general doesn't seem to solve for all solutions out there, after looking at various people's code): If there is a coin value that is equivalent to the target, simply return 1 and call it good.
# Otherwise, take a value in the coins list that is the largest value that is also less than the target, and subtract it from the target over and over again while the difference is positive or until it is zero. Each time a subtraction happens, append the coin to a new list called change_list.
# If the difference reaches zero, return the list. If the difference drops below zero, stop the loop or recursion with the last subtraction value, and make the target the value of the last difference. Repeat what happened before: check for a coin in the coins list for a value that is equal to the target, append it to the change_list, and if none found, check for numbers in decreasing value that is less than that of the target. Start subtracting again. Keep repeating this process till the value of the target is zero.

print(" ")
# ITERATIVE SOLUTION I CREATED THAT DOESN'T FINISH OFF THE PROBLEM PROPERLY. Consider using sorted(coins) instead of max(coins).

def coin_number(target, coins):
    if target in coins:
        return 1

    # create a new list of coins that are only those that are <= target
    coins_less_than_target = [coin for coin in coins if coin <= target]

    # variables
    coin = max(coins_less_than_target)
    change_list = []

    while target - coin >= 0:
        target -= coin
        change_list.append(coin)

        # repeat nearly everything above, except choose a new coin and if target in coins, add to the length of the list.


    return change_list

print(coin_number(100, [10, 5, 35])) # output should be 2

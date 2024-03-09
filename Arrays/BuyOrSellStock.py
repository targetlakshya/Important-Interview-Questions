# Best time to buy and sell stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.


def findMaxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:

            max_profit = prices[i] - min_price
    return max_profit

# Driver Code
prices = [7,1,5,3,6,4,100]
# Function calling
maxProfit = findMaxProfit(prices)
print(maxProfit)
# Best time to buy and sell stock

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
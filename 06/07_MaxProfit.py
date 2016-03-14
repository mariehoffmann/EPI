__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# array of stock prices, return maximum profit that could be done my buying and selling
# precondition: len(prices) > 1
def maxProfit(prices):
    min_price = prices[0]
    profit = prices[1] - min_price
    for p in prices[2:]:
        profit = max(p-min_price, profit)
        min_price = min(min_price, p)
    return profit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(maxProfit(prices))

prices = [110, 105, 90]
print(maxProfit(prices))

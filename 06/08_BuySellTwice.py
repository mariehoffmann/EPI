__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# pre: len(prices) > 3
def maxBuySellTwice(prices):
    if len(prices) < 2:
        return 0
    min1, min2 = 0, 2
    max1, max2 = 1, 3
    min_new = min2
    for i in range(4, len(prices)):

        if prices[i] - prices[min_new] > prices[max2] - prices[min2]:
            if min_new > max2: # let 1st ptrs (partially) overtake 2nd ptrs
                if max(prices[min2], prices[max2]) - prices[min1] > prices[max1]-prices[min1]:
                    max1 = max2 if prices[min2] < prices[max2] else min2
                if prices[max1]-prices[min1] < prices[max2]-prices[min1]:
                    min1, max1 = min2, max2
            min2 = min_new
            max2 = i
        if prices[i] < prices[min2]:
            min_new = i

    profit1, profit2 = prices[max1]-prices[min1], prices[max2]-prices[min2]

    return max([profit1, profit2, profit1+profit2, prices[max2]-min(prices[min1],prices[max1])])


prices = [10, 20, 40, 60, 90]
print(maxBuySellTwice(prices))

prices = [10, 15, 30, 29, 25, 28, 34, 40, 5]
print(maxBuySellTwice(prices))







class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = -1
        highestPrice = -1
        highestProfit = 0
        for price in prices:
            if lowestPrice == -1 or price < lowestPrice:
                lowestPrice = price
                highestPrice = -1
            if lowestPrice != -1 and price > highestPrice and price > lowestPrice:
                highestPrice = price
                if highestPrice - lowestPrice > highestProfit:
                    highestProfit = highestPrice - lowestPrice
            print("Highest Price: ", highestPrice)
            print("Lowest Price: ", lowestPrice)
        return highestProfit




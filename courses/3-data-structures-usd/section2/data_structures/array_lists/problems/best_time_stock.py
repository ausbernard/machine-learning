from typing import List
# Problem: Dynamic Programming - involves breaking down a problem into simpler subproblems and solving each subproblem only once, storing the results for future use. In the context of this problem, a dynamic programming approach would involve maintaining an array to store the maximum profit at each day and using this information to compute the overall maximum profit.
# Algorithm: Greedy (singlepass) - This algorithm is designed to find the maximum profit that can be achieved by buying and selling a stock exactly once. Algorithm ensures that a solution is found in a singlepass.

class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        # check if list is empty
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0  
        
        for price in prices:        #O(n)
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    
    # time: O(n)
    # space: O(1)
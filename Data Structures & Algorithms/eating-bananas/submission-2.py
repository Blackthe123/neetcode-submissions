class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimised
        m = max(piles)
        lo = 1
        hi = m
        lowest = m
        while lo <= hi:
            k = (hi + lo) // 2
            curr_h = 0
            for i in range(len(piles)):
                if k >= piles[i]:
                    curr_h += 1
                elif piles[i] % k:
                    curr_h += (piles[i] // k) + 1
                else:
                    curr_h += piles[i] / k
                if curr_h > h:
                    lo = k + 1
                    break
            if curr_h <= h:
                hi = k - 1
                if k < lowest:
                    lowest = k
        return lowest
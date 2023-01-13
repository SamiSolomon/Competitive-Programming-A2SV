class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        for i in range(len(piles)//3):
            total += piles[-2*i - 2]
        return total

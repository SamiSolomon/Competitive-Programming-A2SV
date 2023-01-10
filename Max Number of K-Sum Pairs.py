class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        f = {}
        for i in nums:
            j = k - i
            if j in f and f[j] > 0:
                result += 1
                f[j] -= 1
            else:
                if i not in f:
                    f[i] = 0
                f[i] +=1
        return result

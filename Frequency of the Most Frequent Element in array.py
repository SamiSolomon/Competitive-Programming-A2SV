class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        answer = 0
        sum = 0
        nums.sort()
        li = 0
        for right, num in enumerate(nums):
            sum += num
            while sum + k < num * (right - li + 1):
                sum -= nums[li]
                li += 1
            answer = max(answer, right - li + 1)

        return answer

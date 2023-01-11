class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def arthemetic(nums):
            if len(nums) < 2:
                return False

            if len(nums) == 2:
                return True
            
            arth =nums[1] - nums[0]
            for i in range(1,len(nums) -1):
                if nums[i + 1] -nums[i] !=arth:
                    return False
            return True

        out = []
        n = len(l)
        for i in range(n):
            s=nums[l[i]: r[i]+1]
            s.sort()
            if arthemetic(s):
                out.append(True)
            else:
                out.append(False)
        
        return out

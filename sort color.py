class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0 
        middle = 0
        right = len(nums) - 1

        while middle <= right:
            if nums[middle] ==0:
                nums[left],nums[middle] = nums[middle],nums[left]
                left +=1
                middle +=1
            elif nums[middle] == 2:
                nums[middle],nums[right] = nums[right],nums[middle]
                right -=1
            else:
                middle +=1


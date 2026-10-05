class Solution:
    # Added 'self' as the first parameter
    def searchInsert(self, nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left+=1
            else:
                right -=1
        return left

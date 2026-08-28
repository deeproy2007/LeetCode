class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 :
            return 0
        nums.sort()
        max_n=0
        for i in range(len(nums)-1):
            diff=nums[i+1] - nums[i]
            if diff >  max_n:
                max_n=diff
        return max_n
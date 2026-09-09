class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_n=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=(nums[i]-1)*(nums[j]-1)
                if p > max_n:
                    max_n= p
        return max_n

        
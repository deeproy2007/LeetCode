class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        t_s=1<<n
        result=[]
        for i in range(t_s):
            subset=[]
            for j in range(n):
                if (i&(1<<j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
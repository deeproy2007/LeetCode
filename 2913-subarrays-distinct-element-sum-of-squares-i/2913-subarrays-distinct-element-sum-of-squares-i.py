class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(n):
            de=set()
            for j in range(i,n):
                de.add(nums[j])
                count=len(de)
                total_sum += count*count
        return total_sum
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        A = []
        B = []

    # FIX: Check every element by using len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                A.append(nums[i])
            else:
                B.append(nums[i])

        nums[:] = A + B
        """
        Do not return anything, modify nums in-place instead.
        """
        
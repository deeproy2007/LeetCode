class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(start):
            # Base case: if we've reached the end of the array, a complete permutation is formed
            if start == len(nums):
                result.append(nums[:])  # Append a copy of the current configuration
                return
            
            for i in range(start, len(nums)):
                # Place the element at index i into the current 'start' position
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations for the remaining elements
                backtrack(start + 1)
                
                # Backtrack: undo the swap to restore the original state for the next iteration
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return result

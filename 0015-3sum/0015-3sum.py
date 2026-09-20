class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array to enable two-pointer strategy and skip duplicates easily
        nums.sort()
        
        for i in range(len(nums)):
            # Optimization: If the current number is greater than 0, 
            # three positive numbers can never sum up to 0. Stop the loop.
            if nums[i] > 0:
                break
                
            # Step 2: Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < 0:
                    left += 1  # Need a larger value
                elif three_sum > 0:
                    right -= 1  # Need a smaller value
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Advance pointers
                    left += 1
                    right -= 1
                    
                    # Step 4: Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res


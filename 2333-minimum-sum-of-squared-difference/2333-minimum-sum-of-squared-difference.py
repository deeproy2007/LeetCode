class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Step 1: Combine budgets and find maximum difference
        k = k1 + k2
        n = len(nums1)
        
        # Track the maximum difference to size our buckets
        max_diff = 0
        diffs = [0] * n
        for i in range(n):
            diffs[i] = abs(nums1[i] - nums2[i])
            if diffs[i] > max_diff:
                max_diff = diffs[i]
                
        # Step 2: Early Exit if we can reduce everything to 0
        if sum(diffs) <= k:
            return 0
            
        # Populate the frequency buckets
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
            
        # Step 3: Flatten the peaks greedily from max_diff down to 1
        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
                
            # Determine how many elements we can decrement at this level
            take = min(k, buckets[d])
            
            buckets[d] -= take
            buckets[d - 1] += take
            k -= take
            
            # If we run out of moves, we can stop early
            if k == 0:
                break
                
        # Step 4: Calculate the final sum of squares
        ans = 0
        for d in range(1, max_diff + 1):
            if buckets[d] > 0:
                ans += buckets[d] * (d ** 2)
                
        return ans


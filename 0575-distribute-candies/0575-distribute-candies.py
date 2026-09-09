class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        # The maximum number of candies the sister can eat
        max_allowed = len(candyType) // 2
        
        # The total number of unique candy types available
        unique_types = len(set(candyType))
        
        # The answer is the smaller of the two values
        return min(max_allowed, unique_types)

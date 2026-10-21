class NumArray:

    def __init__(self, nums: list[int]):
        # prefix array of size N + 1 filled with 0s
        self.prefix = [0] * (len(nums) + 1)
        # Fill the prefix sums
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Returns the range sum in O(1) constant time
        return self.prefix[right + 1] - self.prefix[left]


# --- Driver / Execution Code Example ---
if __name__ == "__main__":
    nums = [3, 1, 4, 2]
    obj = NumArray(nums)
    
    print(obj.sumRange(1, 3))  # Output: 7  (1 + 4 + 2)
    print(obj.sumRange(0, 2))  # Output: 8  (3 + 1 + 4)
    print(obj.sumRange(2, 2))  # Output: 4  (4)
  


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(index, current_combo, current_target):
            # Base Case 1: Successfully hit target
            if current_target == 0:
                res.append(list(current_combo)) # Append a deep copy
                return
            
            # Base Case 2 & 3: Exceeded target or ran out of candidates
            if current_target < 0 or index >= len(candidates):
                return
            
            # Choice 1: Include candidates[index]. 
            # Note: We pass 'index' instead of 'index + 1' to allow re-use.
            current_combo.append(candidates[index])
            backtrack(index, current_combo, current_target - candidates[index])
            
            # The "Backtrack" step: clean up the element before trying the next choice
            current_combo.pop()
            
            # Choice 2: Skip candidates[index] entirely and move forward
            backtrack(index + 1, current_combo, current_target)

        # Start the recursion from the 0th index with an empty combination
        backtrack(0, [], target)
        return res

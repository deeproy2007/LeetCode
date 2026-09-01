class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        
        # Step 2: Build each row level by level
        for i in range(2, rowIndex + 1):
            # Step 3: Loop backwards to update in-place without overwriting data
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
                
        return res
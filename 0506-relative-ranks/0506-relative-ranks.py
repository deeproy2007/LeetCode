class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # 1. Sort the unique scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # 2. Build a rank lookup dictionary
        # Example: {10: "Gold Medal", 9: "Silver Medal", 8: "Bronze Medal", 4: "4"}
        rank_map = {}
        for rank, s in enumerate(sorted_scores):
            if rank == 0:
                rank_map[s] = "Gold Medal"
            elif rank == 1:
                rank_map[s] = "Silver Medal"
            elif rank == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(rank + 1)
        
        # 3. Map the original scores to their ranks
        return [rank_map[s] for s in score]


        
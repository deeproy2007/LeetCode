class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # 4 * n is safe for a 1-indexed complete binary tree layout
        tree_sum = [0] * (4 * n)
        tree_sq_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node: int, length: int, val: int):
            # Transformation: (D + 1)^2 = D^2 + 2D + 1
            tree_sq_sum[node] = (tree_sq_sum[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
            tree_sum[node] = (tree_sum[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node: int, start: int, end: int):
            if lazy[node] == 0:
                return
            val = lazy[node]
            lazy[node] = 0
            
            mid = (start + end) // 2
            apply(2 * node, mid - start + 1, val)
            apply(2 * node + 1, end - mid, val)

        def update(node: int, start: int, end: int, l: int, r: int, val: int):
            if l <= start and end <= r:
                apply(node, end - start + 1, val)
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            
            if l <= mid:
                update(2 * node, start, mid, l, r, val)
            if r > mid:
                update(2 * node + 1, mid + 1, end, l, r, val)
                
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq_sum[node] = (tree_sq_sum[2 * node] + tree_sq_sum[2 * node + 1]) % MOD

        last_seen = {}
        total_ans = 0
        
        for r in range(n):
            l_start = last_seen.get(nums[r], -1) + 1
            update(1, 0, n - 1, l_start, r, 1)
            total_ans = (total_ans + tree_sq_sum[1]) % MOD
            last_seen[nums[r]] = r
            
        return total_ans

        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in nums1:
            for j in nums2:
                if i == j and i not in r:
                    r.append(i)
        return r
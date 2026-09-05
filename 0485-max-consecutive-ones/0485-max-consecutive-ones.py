class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m_c=0
        c_c=0
        for i in nums:
            if i == 1:
                c_c += 1
                if c_c > m_c:
                    m_c=c_c
            else:
                c_c=0
        return m_c

        
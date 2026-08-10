class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        o=x
        r=0
        while o>0:
            digit=o % 10
            r=r*10 + digit
            o=o//10
        if x == r:
            return True
        else:
            return False
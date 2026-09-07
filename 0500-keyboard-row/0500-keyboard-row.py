class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1,row2,row3=set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")
        result=[]
        for i in words:
            w_set=set(i.lower())
            if w_set<=row1 or w_set<=row2 or w_set<=row3:
                result.append(i)
        return result

        
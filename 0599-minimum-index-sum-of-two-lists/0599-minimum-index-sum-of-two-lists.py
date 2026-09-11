class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        p=[]
        for i in list1:
            for j in list2:
                if i == j:
                    p.append(i)
                    return p
        
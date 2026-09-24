class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        result=[]
        top,botton=0,len(matrix) -1
        left,right=0,len(matrix[0])-1
        while top<=botton and left<=right:
            for col in range(left,right+1):
                result.append(matrix[top][col])
            top +=1
            for row in range(top,botton+1):
                result.append(matrix[row][right])
            right -=1
            if top<=botton:
                for col in range(right,left-1,-1):
                    result.append(matrix[botton][col])
                botton -=1
            if left <= right:
                for row in range(botton,top-1,-1):
                    result.append(matrix[row][left])
                left += 1
        return result
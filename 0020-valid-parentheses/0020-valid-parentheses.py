class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in bracket_map:
                te= stack.pop() if stack else '#'
                if bracket_map[char] != te:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

    
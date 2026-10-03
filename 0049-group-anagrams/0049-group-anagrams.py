from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hash map where values default to empty lists
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a character frequency counter for 'a' through 'z'
            count = [0] * 26
            
            for char in s:
                # Find the index (0-25) by subtracting ASCII values
                count[ord(char) - ord('a')] += 1
                
            # Convert the list to a tuple because lists are mutable and cannot be keys
            key = tuple(count)
            
            # Group the original string under this unique letter-count signature
            anagram_map[key].append(s)
            
        # Return all the values grouped together
        return list(anagram_map.values())


# --- Local Test Engine (Optional Code for your IDE) ---
if __name__ == "__main__":
    # Create an instance of the class
    solver = Solution()
    
    # Test Case 1: Standard Example
    test_input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output1 = solver.groupAnagrams(test_input1)
    print(f"Input:  {test_input1}")
    print(f"Output: {output1}\n")
    
    # Test Case 2: Empty String
    test_input2 = [""]
    output2 = solver.groupAnagrams(test_input2)
    print(f"Input:  {test_input2}")
    print(f"Output: {output2}\n")
    
    # Test Case 3: Single Character
    test_input3 = ["a"]
    output3 = solver.groupAnagrams(test_input3)
    print(f"Input:  {test_input3}")
    print(f"Output: {output3}")

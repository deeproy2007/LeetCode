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




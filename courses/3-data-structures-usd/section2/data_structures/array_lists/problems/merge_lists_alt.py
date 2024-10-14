# Algorithm: Sliding Window

import random
import string

class Merge:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        thief = []
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        
        # slide window to the lowest length    
        for chr in range(min_len):
            thief.append(word1[chr])
            thief.append(word2[chr])
        
        # then jump out the window with the remaining length
        if len1 > len2:
            thief.append(word1[min_len:])
        else:
            thief.append(word2[min_len:])

        return ''.join(thief)
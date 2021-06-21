"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

#leetcode
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result=0
        for i in stones:
            if i in jewels:
                result+=1
        return result
"""
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""
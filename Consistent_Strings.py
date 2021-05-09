"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

# code problem source Leetcode
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result=0
        for i in range(0,len(words)):
            flag=1
            for j in range(0,len(words[i])):
                if words[i][j] not in allowed:
                    flag=0
                    break
            if flag==1:
                result=result+1
        return result
                    
        
                    
  """
  Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
  Output: 2
  Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

  """

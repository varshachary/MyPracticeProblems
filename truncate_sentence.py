"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k words. Return s after truncating it.

#Leetcode
"""
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lis=[]
        result=""
        for i in s.split(" "):
            lis.append(i)
        for i in range(0,k):
            result=result+lis[i]
            if i!=k-1:
                result=result+" "
                
        return result
        
"""
Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation:
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".
"""

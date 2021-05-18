"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

#Leetcode
"""
class Solution:
    def sortSentence(self, s: str) -> str:
        res = ""
        di = {}
    
        for word in s.split(" "):
            di[word[-1]] = word[:-1]
            sorted_di=sorted(di)
    
        for key in sorted_di:
            if key == max(sorted_di):
                res += di[key]
            else:
                res += di[key] + " "
    
        return res
        
"""
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

"""

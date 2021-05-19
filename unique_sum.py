"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
#leetcode
"""
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result=0
        leng=len(nums)
        for i in nums:
            if nums.count(i)==1:
                result=result+i
        return result
            
"""
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
"""

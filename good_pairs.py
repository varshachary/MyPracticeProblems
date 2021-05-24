"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
leetcode
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result=0
        counts=Counter(nums)
        for value in counts.values():
            result+=(value*(value-1))//2
        return result
                
   
"""
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""

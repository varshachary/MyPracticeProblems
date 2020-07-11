#Leet Code
"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
""""


class Solution(object):
    def twoSum(self, nums, target):
        lookup={}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
                

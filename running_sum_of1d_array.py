"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
#leetcode
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        result.append(nums[0])
        leng=len(nums)
        for i in range(1,leng):
            result.append(result[i-1]+nums[i])
        return result
 """
 Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
 """

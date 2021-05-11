"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
# source Leetcode
# refrence links- https://www.youtube.com/watch?v=J5IIH35EBVE
#reference link 2 -https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result=0
        n=len(arr)
        for i in range(0,n):
            result=result +(((((n-i)*(i+1))+1)//2)*arr[i])
        return result
            
            
 """
 Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
 """

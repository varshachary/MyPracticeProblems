"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
#source question:Leetcode
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result=0
        n=len(mat[0])
        for i in range(0,len(mat)):
            for j in range (0,n):
                if i==j:
                    result=result+mat[i][j]
                elif j==(n-1)-i and i !=j :
                    result=result+ mat[i][j]
        return result
        
 """
 your input:[[1,2,3],[4,5,6],[7,8,9]]
 output:
25
"""

"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements
"""
#Hackerrank
n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A) - (i in B) for i in sc_ar]))

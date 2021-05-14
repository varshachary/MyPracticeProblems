"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

#source leetcode
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination,origin=set(),set()
        for path in paths:
            origin.add(path[0])
            destination.add(path[1])
        result=(destination-origin)
        return result.pop()
"""
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""

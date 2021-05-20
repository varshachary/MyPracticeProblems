"""

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

#leetcode
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=address.replace('.','[.]')
        return result
"""
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

#!usr/bin/python3

'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

'''

class Solution:
    def isPalindrome(self,x:int)->bool:
        return str(x)==str(x)[::-1]

str1="12345"
str2="1221"
str3="121"
result1=Solution().isPalindrome(str1)
result2=Solution().isPalindrome(str2)
result3=Solution().isPalindrome(str3)
print(result1)
print(result2)
print(result3)


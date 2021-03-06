#! bin/bash/python3

'''
题目描述
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        list1=[]
        maxlen=len(list1)
        while(i<len(s)) :
            if(s[i] not in list1):
                list1.append(s[i])
                if(maxlen<=len(list1)):
                    maxlen=len(list1)
            else :
                index1=list1.index(s[i])
                list1=list1[index1+1:]
                list1.append(s[i])
                if(maxlen<=len(list1)):
                    maxlen=len(list1)
            i=i+1
        return maxlen

str1= "abcdefgabcd"
solution=Solution()
max=solution.lengthOfLongestSubstring(str1)
print (max)

'''
题目难度：中等
一次性用python通过
目前没有看其他题目
十分喜悦，这是我第一次完全用自己的知识在5min之内用python写出来
说明我的python基础课程没有白上！
2021.3.7
```

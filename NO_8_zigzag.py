#! bin/bash/python3
'''
==============================
1.题目说明
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
===============================================================
2021.3.10 
这道题目拖延了比较长时间（24h)
此前我用另外一种方法做，结果对了但是时间效率不是很高，超时
因为用了太多循环语句
===============================================================

'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:return s
        rows=[""]*numRows
        n=2*numRows-2 #keypoint 把Z的一个V看成是一组（找规律）
        for i,char in enumerate(s):
            x=i%n
            rows[min(x,n-x)]+=char

        return ''.join(rows)

s="China Daily"
num=3
example=Solution()
s2=example.convert(s,3)
print(s2)

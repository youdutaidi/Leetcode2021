#! bin/bash/python3

'''
=============================
解法:有两种，回溯法&&动态规划法
感觉有点南，我花了一个小时，还只是抄了代码，但是自己写还是会出问题，周末回来看看。
2021.3.15
比较好的解题思路：
https://leetcode-cn.com/problems/regular-expression-matching/solution/hui-su-he-dong-tai-gui-hua-by-ml-zimingmeng/
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for r in range(1,m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':       # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:                       # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]


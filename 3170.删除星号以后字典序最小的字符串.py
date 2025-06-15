#
# @lc app=leetcode.cn id=3170 lang=python3
#
# [3170] 删除星号以后字典序最小的字符串
#
# https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/description/
#
# algorithms
# Medium (39.64%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 26.1K
# Testcase Example:  '"aaba*"'
#
# 给你一个字符串 s 。它可能包含任意数量的 '*' 字符。你的任务是删除所有的 '*' 字符。
# 当字符串还存在至少一个 '*' 字符时，你可以执行以下操作：
# 删除最左边的 '*' 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
# 请你返回删除所有 '*' 字符以后，剩余字符连接而成的 字典序最小 的字符串。
# 
# 
# 示例 1：
# 输入：s = "aaba*"
# 输出："aab"
# 解释：
# 删除 '*' 号和它左边的其中一个 'a' 字符。如果我们选择删除 s[3] ，s 字典序最小。
# 
# 示例 2：
# 输入：s = "abc"
# 输出："abc"
# 解释：
# 字符串中没有 '*' 字符。
# 
# 
# 提示：
# 1 <= s.length <= 10^5
# s 只含有小写英文字母和 '*' 字符。
# 输入保证操作可以删除所有的 '*' 字符。
# 
#

# @lc code=start
from heapq import heappop, heappush

class Solution:
    def clearStars(self, s: str) -> str:
        # 方法1：优先队列
        # hq = []
        # for i, c in enumerate(s):
        #     if c == '*':
        #         heappop(hq)
        #     else:
        #         heappush(hq, (c, -i))
        # hq.sort(key=lambda e: -e[1])
        # return ''.join(e[0] for e in hq)

        # 方法2：
        base = ord('a')
        stat = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c == '*':
                for rec in stat:
                    if rec:
                        arr[rec.pop()] = '*'
                        break
            else:
                stat[ord(c)-base].append(i)
        return ''.join(c for c in arr if c != '*')

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.clearStars("aaba*")) # "aab"
    print(solution.clearStars("acabac**")) # "acbc"
    print(solution.clearStars("abc")) # "abc"

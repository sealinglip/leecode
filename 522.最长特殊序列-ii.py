#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#
# 给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 - 1 。

# 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。

# s 的 子序列可以通过删去字符串 s 中的某些字符实现。

# 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。


# 示例 1：
# 输入: strs = ["aba", "cdc", "eae"]
# 输出: 3

# 示例 2:
# 输入: strs = ["aaa", "aaa", "aa"]
# 输出: -1


# 提示:
# 2 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] 只包含小写英文字母

from typing import List
# @lc code=start


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubStr(s: str, t: str) -> bool:
            '''
            判断s是否为t的子序列
            '''
            ps = pt = 0
            while ps < len(s) and pt < len(t):
                if s[ps] == t[pt]:
                    ps += 1
                pt += 1
            return ps == len(s)

        res = -1
        for i, s in enumerate(strs):
            unique = True
            for j, t in enumerate(strs):
                if i != j and isSubStr(s, t):
                    unique = False
                    break
            if unique:
                res = max(res, len(s))

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLUSlength(["aba", "cdc", "eae"]))  # 3
    print(solution.findLUSlength(["aaa", "aaa", "aa"]))  # -1

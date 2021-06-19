#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
# 请返回所有可行解 s 中最长长度。

# 示例 1：
# 输入：arr = ["un", "iq", "ue"]
# 输出：4
# 解释：所有可能的串联组合是 "", "un", "iq", "ue", "uniq" 和 "ique"，最大长度为 4。

# 示例 2：
# 输入：arr = ["cha", "r", "act", "ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。

# 示例 3：
# 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26

# 提示：
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] 中只含有小写英文字母

from typing import List
# @lc code=start


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 去掉arr中有重复字符的元素
        arr = [x for x in arr if len(x) == len(set(x))]
        N = len(arr)
        # 求每个字符串的掩码
        mask = [0] * N
        for i, s in enumerate(arr):
            m = 0
            for c in s:
                m |= 1 << (ord(c) - ord('a'))
            mask[i] = m

        maxLen = 0

        def dfs(i: int, curMask: int) -> int:
            if i == N:
                nonlocal maxLen
                maxLen = max(maxLen, bin(curMask).count("1"))
                return

            if (curMask & mask[i]) == 0:
                dfs(i + 1, curMask | mask[i])
            dfs(i + 1, curMask)

        dfs(0, 0)
        return maxLen

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxLength(["un", "iq", "ue"]))
    print(solution.maxLength(["cha", "r", "act", "ers"]))
    print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))

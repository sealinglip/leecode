#
# @lc app=leetcode.cn id=1177 lang=python3
#
# [1177] 构建回文串检测
#
# 给你一个字符串 s，请你对 s 的子串进行检测。

# 每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 重新排列 子串 s[left..right]，并从中选择 最多 k 项替换成任何小写英文字母。
# 如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。
# 返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。
# 注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）


# 示例：
# 输入：s = "abcda", queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
# 输出：[true, false, false, true, true]
# 解释：
# queries[0]: 子串 = "d"，回文。
# queries[1]: 子串 = "bc"，不是回文。
# queries[2]: 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
# queries[3]: 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
# queries[4]: 子串 = "abcda"，可以变成回文的 "abcba"。


# 提示：
# 1 <= s.length, queries.length <= 10 ^ 5
# 0 <= queries[i][0] <= queries[i][1] < s.length
# 0 <= queries[i][2] <= s.length
# s 中只有小写英文字母

# 复习

from typing import List
# @lc code=start


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 子串能重排成回文串的充要条件是奇数字符最多有一个，那么前缀计数只用记奇偶性
        count = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            count[i+1] = count[i] ^ (1 << (ord(c) - ord('a')))

        res = []
        for l, r, k in queries:
            b = (count[r+1] ^ count[l]).bit_count()  # 奇偶性不同的位说明对应字母在本区间是奇数个
            # 替换一次可以消除两个奇数字母
            res.append(b <= 2 * k + 1)

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.canMakePaliQueries("abcda", [[3, 3, 0], [1, 2, 0], [
          0, 3, 1], [0, 3, 2], [0, 4, 1]]))  # [True,False,False,True,True]

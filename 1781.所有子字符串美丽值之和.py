#
# @lc app=leetcode.cn id=1781 lang=python3
#
# [1781] 所有子字符串美丽值之和
#
# 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。

# 比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
# 给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。


# 示例 1：
# 输入：s = "aabcb"
# 输出：5
# 解释：美丽值不为零的字符串包括["aab", "aabc", "aabcb", "abcb", "bcb"] ，每一个字符串的美丽值都为 1 。

# 示例 2：
# 输入：s = "aabcbaa"
# 输出：17


# 提示：
# 1 <= s.length <= 500
# s 只包含小写英文字母。


# @lc code=start
from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            cnt = Counter()
            for j in range(i, n):
                cnt[s[j]] += 1
                res += cnt.most_common(1)[0][1] - min(cnt.values())

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.beautySum("aabcb"))  # 5
    print(solution.beautySum("aabcbaa"))  # 17

#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。


# 示例 1：
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]

# 示例 2：
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]

# 提示：
# 0 <= s.length <= 10^5
# s[i] 为 'A'、'C'、'G' 或 'T'


from typing import List
# @lc code=start
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i: i + L])
        return ans

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRepeatedDnaSequences(
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))  # ["AAAAACCCCC", "CCCCCAAAAA"]
    print(solution.findRepeatedDnaSequences(
        "AAAAAAAAAAAAA"))  # ["AAAAAAAAAA"]

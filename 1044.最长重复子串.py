#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#
# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

# 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。


# 示例 1：
# 输入：s = "banana"
# 输出："ana"

# 示例 2：
# 输入：s = "abcd"
# 输出：""


# 提示：
# 2 <= s.length <= 3 * 10^4
# s 由小写英文字母组成


# @lc code=start
class suffix_array:
    def __init__(self, n: int, m: int, s):
        self.N = 10 ** 5 + 10
        self.n = n
        self.m = m  # 最大的字母，ascii码
        self.s = s
        self.sa = [0 for _ in range(self.N)]  # 排名为i的后缀，开头的index（从1开始计）
        self.rk = [0 for _ in range(self.N)]  # 当前长度下，i开始的后缀的，排名
        self.height = [0 for _ in range(self.N)]  # rk是i-1 和 i 的lcp
        self.x = [0 for _ in range(self.N)]
        self.y = [0 for _ in range(self.N)]
        self.c = [0 for _ in range(self.N)]

    def get_sa(self) -> None:
        for i in range(1, self.n + 1):
            self.x[i] = ord(self.s[i])
            self.c[self.x[i]] += 1
        for i in range(2, self.m + 1):
            self.c[i] += self.c[i - 1]
        for i in range(self.n, 0, -1):
            self.sa[self.c[self.x[i]]] = i
            self.c[self.x[i]] -= 1

        k = 1
        while k <= self.n:
            num = 0
            for i in range(self.n - k + 1, self.n + 1, 1):
                num += 1
                self.y[num] = i
            for i in range(1, self.n + 1):
                if self.sa[i] > k:
                    num += 1
                    self.y[num] = self.sa[i] - k

            for i in range(1, self.m + 1):
                self.c[i] = 0
            for i in range(1, self.n + 1):
                self.c[self.x[i]] += 1
            for i in range(2, self.m + 1):
                self.c[i] += self.c[i - 1]

            for i in range(self.n, 0, -1):
                self.sa[self.c[self.x[self.y[i]]]] = self.y[i]
                self.c[self.x[self.y[i]]] -= 1
                self.y[i] = 0

            self.x, self.y = self.y, self.x
            self.x[self.sa[1]] = 1
            num = 1

            for i in range(2, self.n + 1):
                if (self.y[self.sa[i]] == self.y[self.sa[i - 1]]) and (self.y[self.sa[i] + k] == self.y[self.sa[i - 1] + k]):
                    self.x[self.sa[i]] = num
                else:
                    num += 1
                    self.x[self.sa[i]] = num

            if num == self.n:
                break
            self.m = num

            k *= 2

    def get_height(self) -> None:
        for i in range(1, self.n + 1):
            self.rk[self.sa[i]] = i
        k = 0
        for i in range(1, self.n + 1):
            if self.rk[i] == 1:
                continue
            if k > 0:
                k -= 1
            j = self.sa[self.rk[i] - 1]
            while (i + k <= self.n) and (j + k <= self.n) and (self.s[i + k] == self.s[j + k]):
                k += 1
            self.height[self.rk[i]] = k


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        SA = suffix_array(n, ord('z'), " " + s)
        SA.get_sa()
        SA.get_height()

        res = 0
        idx = -1
        for i in range(1, n + 1):
            if SA.height[i] > res:
                res = SA.height[i]
                idx = SA.sa[i]
        if res == 0:
            return ""
        else:
            return s[idx - 1: idx - 1 + res]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestDupSubstring("banana"))  # "ana"
    print(solution.longestDupSubstring("abcd"))  # ""

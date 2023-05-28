#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#
# 给定一个二进制字符串 s 和一个正整数 n，如果对于[1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。

# 子字符串 是字符串中连续的字符序列。


# 示例 1：
# 输入：s = "0110", n = 3
# 输出：true

# 示例 2：
# 输入：s = "0110", n = 4
# 输出：false


# 提示：
# 1 <= s.length <= 1000
# s[i] 不是 '0' 就是 '1'
# 1 <= n <= 10^9

# 复习

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n == 1:
            return s.find('1') != -1

        sl = len(s)
        k = len(bin(n)) - 3
        if sl < (1 << (k-1)) + k - 1 or sl < n - (1 << k) + k + 1:
            return False

        def traverse(k, mi, ma):
            st = set()
            t = 0
            for r in range(len(s)):
                t = (t << 1) + int(s[r])
                if r >= k:
                    t -= int(s[r - k]) << k
                if r >= k - 1 and t >= mi and t <= ma:
                    st.add(t)
            return len(st) == ma - mi + 1

        return traverse(k, 1 << (k - 1), (1 << k) - 1) and traverse(k + 1, 1 << k, n)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.queryString("1", 1))  # True
    print(solution.queryString("1111000101", 5))  # True
    print(solution.queryString("0110", 3))  # True
    print(solution.queryString("0110", 4))  # False

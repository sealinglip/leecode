#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。

# 示例 1：
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

# 示例 2：
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。

# 提示：
# 1 <= n <= 1690

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        if n == 1:
            return res[n - 1]
        else:
            idx2 = idx3 = idx5 = 0
            for i in range(n - 1):
                res.append(min(res[idx2] * 2, res[idx3] * 3, res[idx5] * 5))
                if res[-1] == res[idx2] * 2:
                    idx2 += 1
                if res[-1] == res[idx3] * 3:
                    idx3 += 1
                if res[-1] == res[idx5] * 5:
                    idx5 += 1
            return res[-1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nthUglyNumber(2))
    print(solution.nthUglyNumber(10))

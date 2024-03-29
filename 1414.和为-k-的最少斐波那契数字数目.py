#
# @lc app=leetcode.cn id=1414 lang=python3
#
# [1414] 和为 K 的最少斐波那契数字数目
#
# 给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

# 斐波那契数字定义为：

# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
# 数据保证对于给定的 k ，一定能找到可行解。


# 示例 1：
# 输入：k = 7
# 输出：2
# 解释：斐波那契数字为：1，1，2，3，5，8，13，……
# 对于 k = 7 ，我们可以得到 2 + 5 = 7 。

# 示例 2：
# 输入：k = 10
# 输出：2
# 解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。

# 示例 3：
# 输入：k = 19
# 输出：3
# 解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。


# 提示：
# 1 <= k <= 10 ^ 9

# @lc code=start
from bisect import bisect_right


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 贪心算法
        # 先得出小于k的所有fibonacci数列
        fibonacci = [1, 1]
        while fibonacci[-1] < k:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

        num = 0
        while k:
            i = bisect_right(fibonacci, k)
            k -= fibonacci[i - 1]
            num += 1
        return num


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinFibonacciNumbers(7))  # 2
    print(solution.findMinFibonacciNumbers(10))  # 2
    print(solution.findMinFibonacciNumbers(19))  # 3

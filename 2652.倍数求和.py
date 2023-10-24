#
# @lc app=leetcode.cn id=2652 lang=python3
#
# [2652] 倍数求和
#
# 给你一个正整数 n ，请你计算在[1，n] 范围内能被 3、5、7 整除的所有整数之和。
# 返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。


# 示例 1：
# 输入：n = 7
# 输出：21
# 解释：在[1, 7] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7 。数字之和为 21 。

# 示例 2：
# 输入：n = 10
# 输出：40
# 解释：在[1, 10] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9、10 。数字之和为 40 。

# 示例 3：
# 输入：n = 9
# 输出：30
# 解释：在[1, 9] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9 。数字之和为 30 。


# 提示：
# 1 <= n <= 10^3

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def f(m: int) -> int:
            '''
            [1, n]中能整除m的数之和
            '''
            return n // m * m * (n // m + 1) // 2
        return f(3) + f(5) + f(7) - f(15) - f(35) - f(21) + f(105)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfMultiples(7))  # 21
    print(solution.sumOfMultiples(10))  # 40
    print(solution.sumOfMultiples(9))  # 30

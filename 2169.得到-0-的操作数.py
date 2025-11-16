#
# @lc app=leetcode.cn id=2169 lang=python3
#
# [2169] 得到 0 的操作数
#
# https://leetcode.cn/problems/count-operations-to-obtain-zero/description/
#
# algorithms
# Easy (73.43%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 34.7K
# Testcase Example:  '2\n3'
#
# 给你两个 非负 整数 num1 和 num2 。
# 每一步 操作 中，如果 num1 >= num2 ，你必须用 num1 减 num2 ；否则，你必须用 num2 减 num1 。
# 
# 例如，num1 = 5 且 num2 = 4 ，应该用 num1 减 num2 ，因此，得到 num1 = 1 和 num2 = 4 。然而，如果
# num1 = 4且 num2 = 5 ，一步操作后，得到 num1 = 4 和 num2 = 1 。
# 
# 返回使 num1 = 0 或 num2 = 0 的 操作数 。
# 
# 
# 示例 1：
# 输入：num1 = 2, num2 = 3
# 输出：3
# 解释：
# - 操作 1 ：num1 = 2 ，num2 = 3 。由于 num1 < num2 ，num2 减 num1 得到 num1 = 2 ，num2 = 3
# - 2 = 1 。
# - 操作 2 ：num1 = 2 ，num2 = 1 。由于 num1 > num2 ，num1 减 num2 。
# - 操作 3 ：num1 = 1 ，num2 = 1 。由于 num1 == num2 ，num1 减 num2 。
# 此时 num1 = 0 ，num2 = 1 。由于 num1 == 0 ，不需要再执行任何操作。
# 所以总操作数是 3 。
# 
# 示例 2：
# 输入：num1 = 10, num2 = 10
# 输出：1
# 解释：
# - 操作 1 ：num1 = 10 ，num2 = 10 。由于 num1 == num2 ，num1 减 num2 得到 num1 = 10 - 10
# = 0 。
# 此时 num1 = 0 ，num2 = 10 。由于 num1 == 0 ，不需要再执行任何操作。
# 所以总操作数是 1 。
# 
# 
# 提示：
# 0 <= num1, num2 <= 10^5
# 
# 复习
#


# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # 辗转相减也会让其中一个数变成两者的gcd，然后用除法就能求出所需次数，关键是让其中一个数变成gcd的次数怎么确定，没有好办法就模拟，但不用减法，实际上除法，大数除以小数
        res = 0
        while num1 and num2:
            res += num1 // num2
            num1 = num1 % num2
            num1, num2 = num2, num1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countOperations(2, 3)) # 3
    print(solution.countOperations(10, 10)) # 1

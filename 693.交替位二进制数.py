#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#
# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。


# 示例 1：
# 输入：n = 5
# 输出：true
# 解释：5 的二进制表示是：101

# 示例 2：
# 输入：n = 7
# 输出：false
# 解释：7 的二进制表示是：111.

# 示例 3：
# 输入：n = 11
# 输出：false
# 解释：11 的二进制表示是：1011.


# 提示：
# 1 <= n <= 2^31 - 1


# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n & 1
        alternating = True
        n >>= 1
        while n:
            flag = 1 - flag
            if n & 1 != flag:
                alternating = False
                break
            n >>= 1

        return alternating


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.hasAlternatingBits(5))  # True
    print(solution.hasAlternatingBits(7))  # False
    print(solution.hasAlternatingBits(11))  # False

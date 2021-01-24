#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#
# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。
# 例如，如果 X = 1231，那么其数组形式为[1, 2, 3, 1]。
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

# 示例 1：
# 输入：A = [1, 2, 0, 0], K = 34
# 输出：[1, 2, 3, 4]
# 解释：1200 + 34 = 1234

# 示例 2：
# 输入：A = [2, 7, 4], K = 181
# 输出：[4, 5, 5]
# 解释：274 + 181 = 455

# 示例 3：
# 输入：A = [2, 1, 5], K = 806
# 输出：[1, 0, 2, 1]
# 解释：215 + 806 = 1021

# 示例 4：
# 输入：A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K = 1
# 输出：[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 解释：9999999999 + 1 = 10000000000

# 提示：
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# 如果 A.length > 1，那么 A[0] != 0

from typing import List
# @lc code=start


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        N = len(A)
        i = -1
        carryOver = 0  # 记录进位
        # while i >= -N:
        while K > 0 or carryOver > 0:
            addend = K % 10
            K = K // 10
            sum = addend + carryOver + (0 if i < -N else A[i])
            if sum >= 10:
                sum -= 10
                carryOver = 1
            else:
                carryOver = 0
            if i < -N:
                A.insert(0, sum)
            else:
                A[i] = sum
            i -= 1

        return A


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.addToArrayForm([1, 2, 0, 0], 34))
    print(solution.addToArrayForm([2, 7, 4], 181))
    print(solution.addToArrayForm([2, 1, 5], 806))
    print(solution.addToArrayForm([1, 5], 1896))
    print(solution.addToArrayForm([1, 5], 9996))
    print(solution.addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))

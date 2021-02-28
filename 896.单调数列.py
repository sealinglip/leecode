#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i] > = A[j]，
# 那么数组 A 是单调递减的。
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。

# 示例 1：
# 输入：[1, 2, 2, 3]
# 输出：true

# 示例 2：
# 输入：[6, 5, 4, 4]
# 输出：true

# 示例 3：
# 输入：[1, 3, 2]
# 输出：false

# 示例 4：
# 输入：[1, 2, 4, 5]
# 输出：true

# 示例 5：
# 输入：[1, 1, 1]
# 输出：true

# 提示：
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000

from typing import List
# @lc code=start


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        N = len(A)
        if N < 3:
            return True

        s = 1
        while A[s] == A[0]:
            s += 1
            if s >= N:
                return True
        trend = A[s] > A[0]  # 得到趋势

        for i in range(s + 1, N):
            if A[i] != A[i - 1] and (trend ^ (A[i] > A[i - 1])):
                return False

        return True


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMonotonic([1, 2, 2, 3]))
    print(solution.isMonotonic([6, 5, 4, 4]))
    print(solution.isMonotonic([1, 3, 2]))
    print(solution.isMonotonic([1, 2, 4, 5]))
    print(solution.isMonotonic([1, 1, 1]))

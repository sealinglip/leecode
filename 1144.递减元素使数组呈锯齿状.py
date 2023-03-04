#
# @lc app=leetcode.cn id=1144 lang=python3
#
# [1144] 递减元素使数组呈锯齿状
#
# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

# 如果符合下列情况之一，则数组 A 就是 锯齿数组：

# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。


# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。

# 示例 2：
# 输入：nums = [9, 6, 1, 6, 2]
# 输出：4


# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000

# 复习

from math import inf
from typing import List
# @lc code=start


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # 只能减的话，直接比较两种情况下的操作数
        # def adjust(b: bool) -> int:
        #     '''
        #     b: 索引0处是峰还是谷
        #     '''
        #     res = 0
        #     pos = 1 if b else 0
        #     n = len(nums)
        #     while pos < n:
        #         left = nums[pos - 1] if pos else inf
        #         right = nums[pos + 1] if pos < n - 1 else inf
        #         res += max(nums[pos] - min(left, right) + 1, 0)
        #         pos += 2
        #     return res
        # return min(adjust(True), adjust(False))

        MI, MA = min(nums)-1, max(nums)+1  # 数组元素的值调整的范围为[MI, MA]
        # 如果考虑可加可减，动规解决
        # 记dp[i][j][k] 为前i个元素调整为锯齿状，调整后第i个元素的值为j，k代表第i个元素是峰（0）还是谷（1），对应的最少调整次数
        # 那么有，dp[i][j][1] = min(dp[i-1][x][0] for x in range(j+1, MA+1)) + abs(nums[i]-j)
        # dp[i][j][0] = min(dp[i-1][x][1] for x in range(MI, j)) + + abs(nums[i]-j)
        # 由于dp[i] 只依赖于dp[i-1]，所以状态可以压缩为二维，即i维可以压缩，另外，j维可以平移标准化（nums[i] - MI)
        # 起始边界条件：dp[j][*] = 0
        span = MA - MI + 1
        dp = [[0, 0] for j in range(span)]
        for i in range(n):
            newDp = [[inf, inf] for _ in range(span)]
            for j, nd in enumerate(newDp):
                nd[0] = min([dp[x][1]
                            for x in range(j)], default=inf) + abs(nums[i]-MI - j)
                nd[1] = min([dp[x][0]
                            for x in range(j+1, span)], default=inf) + abs(nums[i]-MI - j)
            dp = newDp
        return min(min(e) for e in dp)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # print(solution.movesToMakeZigzag([1, 2, 3]))  # 2
    print(solution.movesToMakeZigzag([1, 1, 1]))  # 1
    # print(solution.movesToMakeZigzag([9, 6, 1, 6, 2]))  # 4
    # print(solution.movesToMakeZigzag([10, 4, 4, 10, 10, 6, 2, 3]))  # 13

    # # 如果允许加减
    # print(solution.movesToMakeZigzag([6, 2, 1, 2]))  # 2
    # print(solution.movesToMakeZigzag([3, 10, 7, 10, 9, 10, 6, 9, 4]))  # 0
    # print(solution.movesToMakeZigzag([10, 4, 4, 10, 10, 6, 2, 3]))  # 12

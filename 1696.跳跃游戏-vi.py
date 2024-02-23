#
# @lc app=leetcode.cn id=1696 lang=python3
#
# [1696] 跳跃游戏 VI
#
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

# 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 
# 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。

# 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
# 请你返回你能得到的 最大得分 。


# 示例 1：
# 输入：nums = [1,-1,-2,4,-7,3], k = 2
# 输出：7
# 解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。

# 示例 2：
# 输入：nums = [10,-5,-2,4,0,3], k = 3
# 输出：17
# 解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。

# 示例 3：
# 输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# 输出：0
 
# 提示：
#  1 <= nums.length, k <= 10^5
# -10^4 <= nums[i] <= 10^4

from collections import deque
from typing import List
# @lc code=start

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # 获取和最大子序列，条件是元素之间的差距不能超过k
        # 记dp(i)为0~i的最大得分
        # 状态转移方程为：
        # dp(i) = nums[i] + max(dp(j) for j in range(max(0, i-k), i))
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        st = deque([0])
        for i in range(1, n):
            while st and st[0] < i - k: # 超出窗口范围的
                st.popleft()
            dp[i] = nums[i] + dp[st[0]]
            while st and dp[st[-1]] <= dp[i]:
                st.pop()
            st.append(i)

        return dp[n-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxResult([100,-1,-100,-1,100], 2)) # 198
    print(solution.maxResult([1,-1,-2,4,-7,3], 2)) # 7
    print(solution.maxResult([10,-5,-2,4,0,3], 3)) # 17
    print(solution.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)) # 0
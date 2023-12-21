#
# @lc app=leetcode.cn id=2866 lang=python3
#
# [2866] 美丽塔 II
#
# 给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。

# 你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。

# 如果以下条件满足，我们称这些塔是 美丽 的：

# 1 <= heights[i] <= maxHeights[i]
# heights 是一个 山脉 数组。
# 如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组：

# 对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
# 对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
# 请你返回满足 美丽塔 要求的方案中，高度和的最大值 。

# 示例 1：
# 输入：maxHeights = [5,3,4,1,1]
# 输出：13
# 解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]  
# - heights 是个山脉数组，峰值在 i = 0 处。
# 13 是所有美丽塔方案中的最大高度和。

# 示例 2：
# 输入：maxHeights = [6,5,3,9,2,7]
# 输出：22
# 解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山脉数组，峰值在 i = 3 处。
# 22 是所有美丽塔方案中的最大高度和。

# 示例 3：
# 输入：maxHeights = [3,2,5,5,2,3]
# 输出：18
# 解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山脉数组，最大值在 i = 2 处。
# 注意，在这个方案中，i = 3 也是一个峰值。
# 18 是所有美丽塔方案中的最大高度和。

# 提示：
# 1 <= n == maxHeights <= 10^5
# 1 <= maxHeights[i] <= 10^9

# 复习

from typing import List
# @lc code=start
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        # 假设以i为最高点，记左侧含（i）最大高度和为l[i]，那么递推关系为
        # l[i] = l[i-1] + maxHeights[i] if maxHeights[i] >= maxHeights[i-1]
        # l[i] = l[j] + (i-j) * maxHeights[i] if maxHeights[i] < maxHeights[i-1], 
        # j 为0到i之间最接近但不超过maxHeights[i]的位置
        n = len(maxHeights)
        l = [0] * n
        l[0] = maxHeights[0]
        st = [0] # 单调栈
        for i in range(1, n):
            while st and maxHeights[st[-1]] > maxHeights[i]:
                st.pop()
            if maxHeights[i] >= maxHeights[i-1]:
                l[i] = l[i-1] + maxHeights[i]
            elif st:
                    l[i] = l[st[-1]] + (i-st[-1]) * maxHeights[i]
            else:
                l[i] = (i+1) * maxHeights[i]
            st.append(i)

        # 同理求r[i]：以i为最高点，右侧（含i）的最大高度和
        r = [0] * n
        r[-1] = maxHeights[-1]
        st = [n-1]
        for i in range(n-2, -1, -1):
            while st and maxHeights[st[-1]] > maxHeights[i]:
                st.pop()
            if maxHeights[i] >= maxHeights[i+1]:
                r[i] = r[i+1] + maxHeights[i]
            elif st:
                r[i] = r[st[-1]] + (st[-1]-i) * maxHeights[i]
            else:
                r[i] = (n-i) * maxHeights[i]
            st.append(i)

        return max(h1 + h2 - h for h1, h2, h in zip(l, r, maxHeights))
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSumOfHeights([5,3,4,1,1])) # 13
    print(solution.maximumSumOfHeights([6,5,3,9,2,7])) # 22
    print(solution.maximumSumOfHeights([3,2,5,5,2,3])) # 18
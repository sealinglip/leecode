#
# @lc app=leetcode.cn id=1691 lang=python3
#
# [1691] 堆叠长方体的最大高度
#
# 给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。

# 如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。

# 返回 堆叠长方体 cuboids 可以得到的 最大高度 。


# 示例 1：
# 输入：cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
# 输出：190
# 解释：
# 第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
# 第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
# 第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
# 总高度是 95 + 50 + 45 = 190 。

# 示例 2：
# 输入：cuboids = [[38, 25, 45], [76, 35, 3]]
# 输出：76
# 解释：
# 无法将任何长方体放在另一个上面。
# 选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。

# 示例 3：
# 输入：cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]
# 输出：102
# 解释：
# 重新排列长方体后，可以看到所有长方体的尺寸都相同。
# 你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
# 堆叠长方体的最大高度为 6 * 17 = 102 。


# 提示：
# n == cuboids.length
# 1 <= n <= 100
# 1 <= widthi, lengthi, heighti <= 100

# Hard
# 复习

from functools import cache
from typing import List

# @lc code=start


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 如果两个长方体满足堆叠条件，那么将这两个长方体各自摆放为 宽 ≤ 长 ≤ 高 的姿态，这两个长方体仍然会满足堆叠条件。
        # 证明:
        # c1 c2 满足堆叠条件，那么有 w1 ≤ w2, l1 ≤ l2, h1 ≤ h2，排序后有 w'1 ≤ l'1 ≤ h'1 以及 w'2 ≤ l'2 ≤ h'2
        # 易知 w'1 和 h'2 为这六个维度要素中的最小值和最大值，故有 w'1 ≤ w'2, h'1 ≤ h'2
        # 如果 l'1 ＞ l'2，那么六要素排序为 w'1 ≤ w'2 ≤ l'2 < l'1 ≤ h'1 ≤ h'2
        # 而l'2是c2的第二大维度，根据原始条件w1 ≤ w2, l1 ≤ l2, h1 ≤ h2，不管l'2究竟对应(w2, l2, h2)中的哪一个，c1都应该有两个维度
        # 比l'2小，那么矛盾了。故 l'1 ≤ l'2，c1, c2摆放后仍然满足堆叠条件

        def canPile(c1: List[int], c2: List[int]) -> bool:
            '''
            c1 是否可以堆叠在c2之上
            '''
            return all(c1[i] <= c2[i] for i in range(3))

        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort(key=sum)  # 如果能堆叠，一定sum满足升序；反之不然，sum大不见得一定能堆叠

        # # 方法1：动态规划
        # dp = [0] * n  # dp[i]为以ci为底的最大高度
        # for i, c in enumerate(cuboids):
        #     dp[i] = c[2]
        #     for j in range(i):
        #         if canPile(cuboids[j], c):
        #             dp[i] = max(dp[i], dp[j] + c[2])
        # return max(dp)

        # 方法2：dfs
        @cache
        def dfs(top: int, index: int) -> int:
            '''
            以cuboids[top]为顶，次顶层索引不小于cuboids[index]时，次顶层往下的最大堆叠高度（不含cuboids[top]）
            如图top为-1，表示顶不限制
            '''
            if index == n:
                return 0
            h = dfs(top, index + 1)
            if top == -1 or canPile(cuboids[top], cuboids[index]):
                h = max(h, cuboids[index][2] + dfs(index, index + 1))
            return h
        return dfs(-1, 0)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxHeight(
        [[50, 20, 20], [95, 37, 53], [45, 23, 12]]))  # 145
    # print(solution.maxHeight(
    #     [[50, 45, 20], [95, 37, 53], [45, 23, 12]]))  # 190
    # print(solution.maxHeight([[38, 25, 45], [76, 35, 3]]))  # 76
    # print(solution.maxHeight([[7, 11, 17], [7, 17, 11], [
    #       11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]))  # 102

#
# @lc app=leetcode.cn id=1040 lang=python3
#
# [1040] 移动石子直到连续 II
#
# 在一个长度 无限 的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作 端点石子 。

# 每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。

# 值得注意的是，如果石子像 stones = [1, 2, 5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。

# 当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

# 要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。


# 示例 1：
# 输入：[7, 4, 9]
# 输出：[1, 2]
# 解释：
# 我们可以移动一次，4 -> 8，游戏结束。
# 或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。

# 示例 2：
# 输入：[6, 5, 4, 3, 10]
# 输出：[2, 3]
# 解释：
# 我们可以移动 3 -> 8，接着是 10 -> 7，游戏结束。
# 或者，我们可以移动 3 -> 7, 4 -> 8, 5 -> 9，游戏结束。
# 注意，我们无法进行 10 -> 2 这样的移动来结束游戏，因为这是不合要求的移动。

# 示例 3：
# 输入：[100, 101, 104, 102, 103]
# 输出：[0, 0]


# 提示：
# 3 <= stones.length <= 10 ^ 4
# 1 <= stones[i] <= 10 ^ 9
# stones[i] 的值各不相同。

# 复习

from typing import List
# @lc code=start


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones.sort()
        if stones[-1] - stones[0] == n - 1:  # 已经是连续排列的情况
            return [0, 0]

        max_m = max(stones[-2] - stones[0] + 1, stones[-1] -
                    stones[1] + 1) - (n - 1)  # 最多移动次数就是让空间缩短最慢的方式

        # 移动窗口，用长度为n的窗口从stones的一端移向另一端，窗口中石子最密集的情况就是移动次数最少的
        c = 0  # 记录窗口中的石子数
        r = 0  # 记录窗口在stones中的右边界
        while r < n and stones[r] < stones[0] + n:
            r += 1

        min_m = n - r if r < n - 1 else 2
        l = 0  # 记录窗口在stones中的左边界
        while r < n:
            p = stones[r] - n + 1  # 窗口左边界
            r += 1

            while l < n and stones[l] < p:
                l += 1

            if r - l == n - 1 and stones[r-1] - stones[l] == n - 2:
                min_m = min(min_m, 2)
            else:
                min_m = min(min_m, n - r + l)

        return [min_m, max_m]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numMovesStonesII([7, 4, 9]))  # [1,2]
    print(solution.numMovesStonesII([8, 7, 6, 5, 2]))  # [2,2]
    print(solution.numMovesStonesII([6, 5, 4, 3, 10]))  # [2,3]
    print(solution.numMovesStonesII([100, 101, 104, 102, 103]))  # [0,0]

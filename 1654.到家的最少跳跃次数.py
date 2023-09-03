#
# @lc app=leetcode.cn id=1654 lang=python3
#
# [1654] 到家的最少跳跃次数
#
# 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。

# 跳蚤跳跃的规则如下：

# 它可以 往前 跳恰好 a 个位置（即往右跳）。
# 它可以 往后 跳恰好 b 个位置（即往左跳）。
# 它不能 连续 往后跳 2 次。
# 它不能跳到任何 forbidden 数组中的位置。
# 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。

# 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 - 1 。


# 示例 1：
# 输入：forbidden = [14, 4, 18, 1, 15], a = 3, b = 15, x = 9
# 输出：3
# 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。

# 示例 2：
# 输入：forbidden = [8, 3, 16, 6, 12, 20], a = 15, b = 13, x = 11
# 输出：- 1

# 示例 3：
# 输入：forbidden = [1, 6, 2, 14, 5, 17, 4], a = 16, b = 9, x = 7
# 输出：2
# 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。


# 提示：
# 1 <= forbidden.length <= 1000
# 1 <= a, b, forbidden[i] <= 2000
# 0 <= x <= 2000
# forbidden 中所有位置互不相同。
# 位置 x 不在 forbidden 中。

# 复习

from collections import deque
from typing import List
# @lc code=start


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        forbidden = set(forbidden)
        ub = max(max(forbidden) + a, x) + b
        qu = deque([(0, 0, -1)])  # 分别是位置，步数和前一步是否向前
        visited = set([0])

        # 广度优先搜索
        while qu:
            pos, step, prevForward = qu.popleft()

            t = pos + a
            if t == x:
                return step + 1
            elif t not in visited and t not in forbidden and 0 <= t <= ub:
                qu.append((t, step + 1, 1))
                visited.add(t)

            if prevForward == 1:
                t = pos - b
                if t == x:
                    return step + 1
                elif -t not in visited and t not in forbidden and 0 <= t <= ub:
                    qu.append((t, step + 1, -1))
                    visited.add(-t)

        return -1


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumJumps([162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
          154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98], 29, 98, 80))  # 121
    # print(solution.minimumJumps([14, 4, 18, 1, 15], 3, 15, 9))  # 3
    # print(solution.minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11))  # -1
    # print(solution.minimumJumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7))  # 2

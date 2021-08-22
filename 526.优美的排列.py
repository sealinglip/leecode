#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#
# 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位(1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

# 第 i 位的数字能被 i 整除
# i 能被第 i 位上的数字整除
# 现在给定一个整数 N，请问可以构造多少个优美的排列？

# 示例1:
# 输入: 2
# 输出: 2
# 解释:
# 第 1 个优美的排列是[1, 2]:
#   第 1 个位置（i = 1）上的数字是1，1能被 i（i = 1）整除
#   第 2 个位置（i = 2）上的数字是2，2能被 i（i = 2）整除
# 第 2 个优美的排列是[2, 1]:
#   第 1 个位置（i = 1）上的数字是2，2能被 i（i = 1）整除
#   第 2 个位置（i = 2）上的数字是1，i（i = 2）能被 1 整除
# 说明:
# N 是一个正整数，并且不会超过15。

# @lc code=start
from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        ca = defaultdict(list)  # 记录每个数位的可选值
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    ca[i].append(j)

        cnt = 0
        mask = 0

        def backtrack(i: int) -> None:
            if i == n + 1:  # 找到了一个优美排列
                nonlocal cnt
                cnt += 1
                return

            nonlocal mask
            for x in ca[i]:
                flag = 1 << x
                if (mask & flag) == 0:
                    mask |= flag
                    backtrack(i + 1)
                    mask &= ~flag

        backtrack(1)

        return cnt
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.countArrangement(2))

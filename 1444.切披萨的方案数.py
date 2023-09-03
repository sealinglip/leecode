#
# @lc app=leetcode.cn id=1444 lang=python3
#
# [1444] 切披萨的方案数
#
# 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。

# 切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。

# 请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10 ^ 9 + 7 取余的结果。


# 示例 1：
# 输入：pizza = ["A..", "AAA", "..."], k = 3
# 输出：3
# 解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。

# 示例 2：
# 输入：pizza = ["A..", "AA.", "..."], k = 3
# 输出：1

# 示例 3：
# 输入：pizza = ["A..", "A..", "..."], k = 1
# 输出：1


# 提示：
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza 只包含字符 'A' 和 '.' 。

# Hard

from typing import List
# @lc code=start


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        # 每次切都是剩下右下角的块，如果右下角的块上的苹果不够剩余切分需求，则解不成立
        # 先构造二维后缀和
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0] * (cols+1) for _ in range(rows + 1)]
        dp = [[[0] * cols for _ in range(rows)] for _ in range(k + 1)]

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                apples[r][c] = (pizza[r][c] == 'A') + apples[r][c+1] + \
                    apples[r+1][c] - apples[r+1][c+1]
                dp[1][r][c] = 1 if apples[r][c] > 0 else 0

        for i in range(1, k + 1):
            for r in range(rows):
                for c in range(cols):
                    # 横切
                    for j in range(r+1, rows):
                        if apples[r][c] > apples[j][c]:
                            dp[i][r][c] += dp[i-1][j][c]
                    # 竖切
                    for j in range(c+1, cols):
                        if apples[r][c] > apples[r][j]:
                            dp[i][r][c] += dp[i-1][r][j]

                    dp[i][r][c] = dp[i][r][c] % MOD

        return dp[k][0][0]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.ways(["A..", "AAA", "..."], 3))  # 3
    print(solution.ways(["A..", "AA.", "..."], 3))  # 1
    print(solution.ways(["A..", "A..", "..."], 1))  # 1

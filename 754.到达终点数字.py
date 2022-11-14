#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。

# 你可以做一些数量的移动 numMoves:

# 每次你可以选择向左或向右移动。
# 第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
# 给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves) 。


# 示例 1:
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 - 1 。
# 第三次移动，从 - 1 到 2 。

# 示例 2:
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。


# 提示:
# -10^9 <= target <= 10^9
# target != 0

# 复习

# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        # 下面这种搞法会TLE，没有剪枝
        # if target == 0:
        #     return 0
        # pos = set([0])
        # step = 0
        # # 广度优先遍历
        # while True:
        #     step += 1
        #     pos = set([p + step for p in pos] + [p - step for p in pos])
        #     if target in pos:
        #         return step

        target = abs(target)
        step = 0
        while target > 0:
            step += 1
            target -= step
        return step if target % 2 == 0 else step + 1 + (step % 2)

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.reachNumber(-1000000000))  # 44723
    print(solution.reachNumber(2))  # 3
    print(solution.reachNumber(3))  # 2

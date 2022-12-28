#
# @lc app=leetcode.cn id=1739 lang=python3
#
# [1739] 放置盒子
#
# 有一个立方体房间，其长度、宽度和高度都等于 n 个单位。请你在房间里放置 n 个盒子，每个盒子都是一个单位边长的立方体。
# 放置规则如下：

# 你可以把盒子放在地板上的任何地方。
# 如果盒子 x 需要放置在盒子 y 的顶部，那么盒子 y 竖直的四个侧面都 必须 与另一个盒子或墙相邻。
# 给你一个整数 n ，返回接触地面的盒子的 最少 可能数量。


# 示例 1：
# 输入：n = 3
# 输出：3
# 解释：上图是 3 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应左侧位置。

# 示例 2：
# 输入：n = 4
# 输出：3
# 解释：上图是 3 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应左侧位置。

# 示例 3：
# 输入：n = 10
# 输出：6
# 解释：上图是 10 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应后方位置。


# 提示：
# 1 <= n <= 10^9

# Hard

# @lc code=start
class Solution:
    def minimumBoxes(self, n: int) -> int:
        # 记f(i) 为满铺i层的盒子个数
        # 可知f(1) = 1
        # f(2) = 4
        # f(3) = 10
        # f(i) = f(i-1) + i * (i + 1) // 2
        fp, fc, i = 0, 1, 1
        while fc < n:
            i += 1
            fp, fc = fc, fc + i * (i+1) // 2

        if n == fc:
            return fc - fp
        else:
            # (m-1) * m // 2 < (n - fp) <= m * (m+1) // 2
            # return fp + m
            base = (i-1) * i // 2  # 对应fc的底
            i = m = 1
            delta = n - fp
            while m < delta:
                i += 1
                m += i
            return base + i


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumBoxes(15))  # 9
    print(solution.minimumBoxes(3))  # 3
    print(solution.minimumBoxes(4))  # 3
    print(solution.minimumBoxes(10))  # 6

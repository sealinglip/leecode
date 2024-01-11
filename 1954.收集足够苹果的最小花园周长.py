#
# @lc app=leetcode.cn id=1954 lang=python3
#
# [1954] 收集足够苹果的最小花园周长
#
# 给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 (i, j) 处的苹果树有 |i| + |j| 个苹果。

# 你将会买下正中心坐标是 (0, 0) 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。

# 给你一个整数 neededApples ，请你返回土地的 最小周长 ，使得 至少 有 neededApples 个苹果在土地 里面或者边缘上。

# |x| 的值定义为：

# 如果 x >= 0 ，那么值为 x
# 如果 x < 0 ，那么值为 -x
 

# 示例 1：
# 输入：neededApples = 1
# 输出：8
# 解释：边长长度为 1 的正方形不包含任何苹果。
# 但是边长为 2 的正方形包含 12 个苹果（如上图所示）。
# 周长为 2 * 4 = 8 。

# 示例 2：
# 输入：neededApples = 13
# 输出：16
# 示例 3：

# 输入：neededApples = 1000000000
# 输出：5040
 
# 提示：
# 1 <= neededApples <= 10^15

# @lc code=start
from bisect import bisect_left
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # 记dp(i)为正方形边长为2i时包含的苹果数
        # 有dp(0) = 0
        # dp(i) = dp(i-1) + (i * 2 - 1) * 4 * i + (1 + i) * i * 4 （ i > 0 )
        #       = dp(i-1) + 12 * i^2
        #       = 12 * sum(j^2 for j in range(i+1))
        #       = 2 * i * (i + 1) * (2 * i + 1)
        # 边长为2i时，周长为8i
        i = bisect_left(range(10 ** 5), neededApples, key=lambda x: (x + 1) * (1 + (x << 1)) * (x << 1))

        return i << 3
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumPerimeter(1)) # 8
    print(solution.minimumPerimeter(13)) # 16
    print(solution.minimumPerimeter(1000000000)) # 5040

#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#
# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

 
# 示例 1：
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
# 如果它没碎，那么肯定能得出 f = 2 。 
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 

# 示例 2：
# 输入：k = 2, n = 6
# 输出：3

# 示例 3：
# 输入：k = 3, n = 14
# 输出：4
 

# 提示：
# 1 <= k <= 100
# 1 <= n <= 10^4

# Hard
# 复习

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp(k, n) = 1 + min(max(dp(k-1, x-1), dp(k, n-x)) for x in range(1,n+1))
        # 取到最优值的x随n单调递增
        dp = list(range(n+1)) # 初始k = 1, dp[i] 代表 dp(1, i)
        tmp = [0] * (n+1)
        for _ in range(2, k+1):
            x = 1
            for m in range(1, n+1):
                # 计算tmp[m] = dp(j, m)
                # 注意 x在到最优点前，max(dp[x-1], tmp[m-x]) > max(dp[x], tmp[m-x-1])
                while x < m and max(dp[x-1], tmp[m-x]) > max(dp[x], tmp[m-x-1]):
                    x += 1
                tmp[m] = 1 + max(dp[x-1], tmp[m-x])

            dp = tmp[:] # 此时k=j, dp[i]代表dp(j, i)
        
        return dp[-1]

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.superEggDrop(1, 2)) # 2
    print(solution.superEggDrop(2, 6)) # 3
    print(solution.superEggDrop(3, 14)) # 4

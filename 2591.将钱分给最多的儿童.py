#
# @lc app=leetcode.cn id=2591 lang=python3
#
# [2591] 将钱分给最多的儿童
#
# 给你一个整数 money ，表示你总共有的钱数（单位为美元）和另一个整数 children ，表示你要将钱分配给多少个儿童。

# 你需要按照如下规则分配：

# 所有的钱都必须被分配。
# 每个儿童至少获得 1 美元。
# 没有人获得 4 美元。
# 请你按照上述规则分配金钱，并返回 最多 有多少个儿童获得 恰好 8 美元。如果没有任何分配方案，返回 - 1 。


# 示例 1：
# 输入：money = 20, children = 3
# 输出：1
# 解释：
# 最多获得 8 美元的儿童数为 1 。一种分配方案为：
# - 给第一个儿童分配 8 美元。
# - 给第二个儿童分配 9 美元。
# - 给第三个儿童分配 3 美元。
# 没有分配方案能让获得 8 美元的儿童数超过 1 。

# 示例 2：
# 输入：money = 16, children = 2
# 输出：2
# 解释：每个儿童都可以获得 8 美元。


# 提示：
# 1 <= money <= 200
# 2 <= children <= 30

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        rest = money - children  # 每人先给1美元
        if rest < 0:
            return -1
        # 剩下的钱按7元分，能分几份就是几个恰好8元的（需要考虑余数为3或者所有人都分了7元，还有剩余的情况）
        cnt, remainder = divmod(rest, 7)
        if cnt > children or (cnt == children and remainder > 0):
            return children - 1
        elif remainder == 3 and cnt == children - 1:
            return max(0, cnt - 1)
        else:
            return cnt


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.distMoney(13, 3))  # 1
    print(solution.distMoney(5, 2))  # 0
    print(solution.distMoney(1, 5))  # -1
    print(solution.distMoney(20, 3))  # 1
    print(solution.distMoney(16, 2))  # 2

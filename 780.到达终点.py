#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#
# 给定四个整数 sx, sy ，tx 和 ty，如果通过一系列的转换可以从起点(sx, sy) 到达终点(tx, ty)，则返回 true，否则返回 false。

# 从点(x, y) 可以转换到(x, x+y)  或者(x+y, y)。


# 示例 1:
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: true
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)

# 示例 2:
# 输入: sx = 1, sy = 1, tx = 2, ty = 2
# 输出: false

# 示例 3:
# 输入: sx = 1, sy = 1, tx = 1, ty = 1
# 输出: true


# 提示:
# 1 <= sx, sy, tx, ty <= 10^9

# Hard
# 复习，此题逻辑很简单，就是容易TLE
# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # 从题目条件可知，sx、sy、tx、ty一定大于0，那么从tx、ty倒推即可
        while tx > sx and ty > sy and tx != ty:
            # 几次TLE表明，这样减，见效慢，应该一步干到位
            # tx = tx - ty
            if ty < tx:
                tx %= ty
            elif ty > tx:
                ty %= tx

        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.reachingPoints(9, 5, 12, 8))  # False
    print(solution.reachingPoints(2, 2, 1000000000, 2))  # True
    print(solution.reachingPoints(2, 2, 1000000000, 4))  # False
    print(solution.reachingPoints(1, 1, 1000000000, 1))  # True
    print(solution.reachingPoints(9, 10, 9, 19))  # True
    print(solution.reachingPoints(1, 1, 3, 5))  # True
    print(solution.reachingPoints(1, 1, 2, 2))  # False
    print(solution.reachingPoints(1, 1, 1, 1))  # True

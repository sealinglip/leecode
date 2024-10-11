#
# @lc app=leetcode.cn id=1227 lang=python3
#
# [1227] 飞机座位分配概率
#
# 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。

# 剩下的乘客将会：

# 如果他们自己的座位还空着，就坐到自己的座位上，

# 当他们自己的座位被占用时，随机选择其他座位
# 第 n 位乘客坐在自己的座位上的概率是多少？


# 示例 1：
# 输入：n = 1
# 输出：1.00000
# 解释：第一个人只会坐在自己的位置上。

# 示例 2：
# 输入: n = 2
# 输出: 0.50000
# 解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
 

# 提示：
# 1 <= n <= 10^5

# @lc code=start
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # 记本函数为f(x)
        # f(1) = 1
        # f(2) = 0.5
        # 当x > 2 时，第一个乘客随机选座，有1/x的概率还是选到自己的座，此种情况下后续第 n 位乘客坐在自己的座位上的概率是1；
        # 如果第一个乘客没有选到自己的座，选到第i位乘客的座（x > i > 1)，那么后续第 n 位乘客坐在自己的座位上的概率是f(x-i+1)
        # 上述情况不需要包括i = x的情况，因为此种情况，最后的概率为0
        # f(x) = (sum(f(x-i+1) for i in range(2, x)) + 1) / x
        # 又 f(1) = 1，所以上式可以改写为
        # f(x) = sum(f(x) for i in range(1, x)) / x
        # 上式为递推式，左右都乘以x
        # x·f(x) = sum(f(x) for i in range(1, x)) = f(x-1) + (x-1)·f(x-1) = x·f(x-1)
        # 得 f(x) = f(x-1), if x > 2

        return 1.0 if n == 1 else 0.5

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.nthPersonGetsNthSeat(1)) # 1.00000
    print(solution.nthPersonGetsNthSeat(2)) # 0.50000
    print(solution.nthPersonGetsNthSeat(3)) # 0.50000

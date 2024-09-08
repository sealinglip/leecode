# 给你有一个 非负 整数 k 。有一个无限长度的台阶，最低 一层编号为 0 。
# Alice 有一个整数 jump ，一开始值为 0 。Alice 从台阶 1 开始，可以使用 任意 次操作，目标是到达第 k 级台阶。假设 Alice 位于台阶 i ，一次 操作 中，Alice 可以：
# 向下走一级到 i - 1 ，但该操作 不能 连续使用，如果在台阶第 0 级也不能使用。
# 向上走到台阶 i + 2^jump 处，然后 jump 变为 jump + 1 。
# 请你返回 Alice 到达台阶 k 处的总方案数。

# 注意，Alice 可能到达台阶 k 处后，通过一些操作重新回到台阶 k 处，这视为不同的方案。


# 示例 1：
# 输入：k = 0
# 输出：2
# 解释：
# 2 种到达台阶 0 的方案为：
# Alice 从台阶 1 开始。
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# Alice 从台阶 1 开始。
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 执行第二种操作，向上走 2^0 级台阶到台阶 1 。
# 执行第一种操作，从台阶 1 向下走到台阶 0 。

# 示例 2：
# 输入：k = 1
# 输出：4
# 解释：
# 4 种到达台阶 1 的方案为：
# Alice 从台阶 1 开始，已经到达台阶 1 。
# Alice 从台阶 1 开始。
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 执行第二种操作，向上走 2^0 级台阶到台阶 1 。
# Alice 从台阶 1 开始。
# 执行第二种操作，向上走 2^0 级台阶到台阶 2 。
# 执行第一种操作，向下走 1 级台阶到台阶 1 。
# Alice 从台阶 1 开始。
# 执行第一种操作，从台阶 1 向下走到台阶 0 。
# 执行第二种操作，向上走 2^0 级台阶到台阶 1 。
# 执行第一种操作，向下走 1 级台阶到台阶 0 。
# 执行第二种操作，向上走 2^1 级台阶到台阶 2 。
# 执行第一种操作，向下走 1 级台阶到台阶 1 。
 
# 提示：
# 0 <= k <= 10^9

# Hard

from math import factorial


class Solution:
    def waysToReachStair(self, k: int) -> int:
        # 如果第二种操作做了n次，那么通过第二种操作往上跳的级数为：
        # 2^0 + …… + 2^(n-1) = 2^n - 1
        # 假设第二种操作做了n次，有n+1个位置可以安排第一种操作且保证第一种操作不连续
        # 设第一种操作做了m次，那么m <= n+1
        # 且有  2^n - m = k, m <= n+1
        # 对于给定的m、n，方案数为 C(m, n+1)
        # 所以，先解m、n，然后计算每种m、n的方案数，相加得到结果
        def findHighestN(k: int) -> int:
            tmp = k
            n = 0
            while k > 1:
                k >>= 1
                n += 1
            if (1 << n) < tmp:
                n += 1
            return n

        res = 0
        # 2^n >= k
        n = findHighestN(k)
        while True:
            m = (1 << n) - k
            if m > n + 1:
                break
            res += factorial(n+1) / (factorial(m) * factorial(n-m+1))
            n += 1

        return int(res)

if __name__ == "__main__":
    solution = Solution()
    print(solution.waysToReachStair(0)) # 2
    print(solution.waysToReachStair(1)) # 4
    print(solution.waysToReachStair(3)) # 3

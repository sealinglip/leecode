#
# @lc app=leetcode.cn id=2517 lang=python3
#
# [2517] 礼盒的最大甜蜜度
#
# 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。

# 商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。

# 返回礼盒的 最大 甜蜜度。


# 示例 1：
# 输入：price = [13, 5, 1, 8, 21, 2], k = 3
# 输出：8
# 解释：选出价格分别为[13, 5, 21] 的三类糖果。
# 礼盒的甜蜜度为 min(| 13 - 5|, | 13 - 21|, | 5 - 21|) = min(8, 8, 16) = 8 。
# 可以证明能够取得的最大甜蜜度就是 8 。

# 示例 2：
# 输入：price = [1, 3, 1], k = 2
# 输出：2
# 解释：选出价格分别为[1, 3] 的两类糖果。
# 礼盒的甜蜜度为 min(| 1 - 3|) = min(2) = 2 。
# 可以证明能够取得的最大甜蜜度就是 2 。

# 示例 3：
# 输入：price = [7, 7, 7, 7], k = 2
# 输出：0
# 解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。


# 提示：
# 1 <= price.length <= 10^5
# 1 <= price[i] <= 10^9
# 2 <= k <= price.length

from math import inf
from typing import List
# @lc code=start


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def count(step: int) -> int:
            s = -inf
            res = 0
            for p in price:
                if p >= s:
                    res += 1
                    s = p + step
            return res

        # 选k个，就是有k-1个间隔，最大甜蜜度不超过 (price[-1] - price[0]) / (k-1)
        r = (price[-1] - price[0]) // (k-1)
        l = 0
        while l <= r:
            mid = (l + r) >> 1
            c = count(mid)
            if c < k:
                r = mid - 1
            elif c > k:
                l = mid + 1
            else:
                # 此时mid肯定可以，但未必是最大
                l = mid
                while l <= r:
                    mid = (l + r) >> 1
                    c = count(mid)
                    if c < k:
                        r = mid - 1
                    else:
                        l = mid + 1
                break

        return r


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumTastiness([1, 1000000000], 2))  # 999999999
    print(solution.maximumTastiness([13, 5, 1, 8, 21, 2], 3))  # 8
    print(solution.maximumTastiness([1, 3, 1], 2))  # 2
    print(solution.maximumTastiness([7, 7, 7, 7], 2))  # 0

#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#
# 给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：

# 有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
# 只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
# 返回 图中最大连通组件的大小 。


# 示例 1：
# 输入：nums = [4, 6, 15, 35]
# 输出：4

# 示例 2：
# 输入：nums = [20, 50, 9, 63]
# 输出：2

# 示例 3：
# 输入：nums = [2, 3, 6, 7, 4, 12, 21, 39]
# 输出：8


# 提示：
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^5
# nums 中所有值都 不同

# 并查集

from collections import defaultdict
from typing import List
# @lc code=start


class UnionFind:
    def __init__(self):
        self.group = {}
        self.count = defaultdict(int)

    def find(self, x: int) -> int:
        if (grpX := self.group.get(x, x)) != x:
            if self.group.get(grpX, grpX) != grpX:
                self.group[x] = self.find(grpX)
        return self.group.get(x, x)

    def merge(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.group[x] = y
            self.count[y] += self.count[x]

    def record(self, x: int) -> int:
        self.count[self.find(x)] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # nums中的数字的范围是[1, 10 ** 5]，其质因子最大就是359
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                  167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359]

        uf = UnionFind()
        for num in nums:
            maxp = num >> 1
            tmp = num
            for p in primes:
                if p > maxp or p > tmp:
                    break
                while tmp % p == 0:
                    tmp //= p
                    uf.merge(num, p)
                    if tmp > 1:
                        uf.merge(tmp, p)
            uf.record(num)

        return max(uf.count.values())

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()

    print(solution.largestComponentSize([2, 7, 522, 526, 535, 26, 944, 35, 519, 45, 48, 567, 266, 68, 74, 591, 81, 86, 602, 93, 610, 621, 111, 114, 629, 641, 131, 651, 142, 659, 669, 161, 674, 163, 180, 187, 190, 194, 195, 206, 207, 218, 737, 229, 240, 757, 770,
                                         260, 778, 270, 272, 785, 274, 290, 291, 292, 296, 810, 816, 314, 829, 833, 841, 349, 880, 369, 147, 897, 387, 390, 905, 405, 406, 407, 414, 416, 417, 425, 938, 429, 432, 926, 959, 960, 449, 963, 966, 929, 457, 463, 981, 985, 79, 487, 1000, 494, 508]))  # 84
    print(solution.largestComponentSize([4, 6, 15, 35]))  # 4
    print(solution.largestComponentSize([20, 50, 9, 63]))  # 2
    print(solution.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))  # 8
    print(solution.largestComponentSize([2, 39, 156]))  # 3

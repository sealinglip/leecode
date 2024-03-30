#
# @lc app=leetcode.cn id=823 lang=python3
#
# [823] 带因子的二叉树
#
# 给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。

# 用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。

# 满足条件的二叉树一共有多少个？答案可能很大，返回 对 10^9 + 7 取余 的结果。


# 示例 1:
# 输入: arr = [2, 4]
# 输出: 3
# 解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]

# 示例 2:
# 输入: arr = [2, 4, 5, 10]
# 输出: 7
# 解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


# 提示：
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 10^9
# arr 中的所有值 互不相同

from collections import defaultdict
from functools import cache
from itertools import combinations
from typing import List
# @lc code=start


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # 满足条件的二叉树一定是完全二叉树
        # 所有的单结点树都满足条件
        # 找出所有的非叶结点值（即可以分解成两个数乘积，这两个数都在集合中）
        n = len(arr)
        prod = {}
        for i in range(n):
            for j in range(i, n):
                prod[(arr[i], arr[j])] = arr[i] * arr[j]

        validProd = set(arr).intersection(prod.values())
        # 转换为非叶节点和可拆分方式的映射
        possibleParent = defaultdict(list)
        for k, v in prod.items():
            if v in validProd:
                possibleParent[v].append(k)

        @cache
        def btree(root: int) -> int:
            """返回以root为根的满足条件的树有多少种"""
            if root in possibleParent:
                res = 1  # 什么子节点都不大的情况
                for c1, c2 in possibleParent[root]:
                    # 如果 c1 != c2，左右互换是双倍可能
                    res += btree(c1) * btree(c2) * (1 if c1 == c2 else 2)
                res %= MOD
                return res
            else:
                return 1

        return sum(btree(x) for x in arr) % MOD

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numFactoredBinaryTrees([2, 4]))  # 3
    print(solution.numFactoredBinaryTrees([2, 4, 5, 10]))  # 7

#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
#
# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：

# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

# 如果一个节点有 0 个子节点，那么该节点为叶节点。


# 示例 1：
# 输入：arr = [6, 2, 4]
# 输出：32
# 解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。

# 示例 2：
# 输入：arr = [4, 11]
# 输出：44


# 提示：
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# 答案保证是一个 32 位带符号整数，即小于 2^31 。

# 复习

from functools import cache
from math import inf
from typing import List, Tuple
# @lc code=start


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # 记忆化搜索
        # @cache
        # def mct(s: int, e: int) -> Tuple[int, int]:
        #     if e - s == 1:
        #         return 0, arr[s]
        #     elif e - s == 2:
        #         return arr[s] * arr[s+1], max(arr[s], arr[s+1])
        #     else:
        #         ma = max(arr[s:e])
        #         mis = inf
        #         for j in range(1, e-s):
        #             mct1 = mct(s, s+j)
        #             mct2 = mct(s+j, e)
        #             mis = min(mis, mct1[0] + mct2[0] + mct1[1] * mct2[1])
        #         return mis, ma

        # return mct(0, len(arr))[0]

        # 单调栈
        st = []
        cost = 0
        for n in arr:
            if not st or n < st[-1]:
                st.append(n)
            else:
                t = st.pop()
                while st and st[-1] < n:
                    cost += st[-1] * t
                    t = st.pop()
                cost += t * n
                st.append(n)
        for i in range(len(st) - 1):
            cost += st[i] * st[i+1]

        return cost

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.mctFromLeafValues([15, 13, 5, 3, 15]))  # 500
    print(solution.mctFromLeafValues([6, 2, 4]))  # 32
    print(solution.mctFromLeafValues([4, 11]))  # 44

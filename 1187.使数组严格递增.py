#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#
# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。

# 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。

# 如果无法让 arr1 严格递增，请返回 - 1。


# 示例 1：
# 输入：arr1 = [1, 5, 3, 6, 7], arr2 = [1, 3, 2, 4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。

# 示例 2：
# 输入：arr1 = [1, 5, 3, 6, 7], arr2 = [4, 3, 1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。

# 示例 3：
# 输入：arr1 = [1, 5, 3, 6, 7], arr2 = [1, 6, 3, 3]
# 输出：- 1
# 解释：无法使 arr1 严格递增。


# 提示：
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10 ^ 9

# Hard
# 复习

from bisect import bisect_left
from functools import cache
from math import inf
from typing import List
# @lc code=start


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 要保证arr1严格递增，实际上从arr2选择元素是不放回采样——如果采同一个元素多次，那么替换后的arr1不可能严格递增
        a = arr1 + [inf]
        b = sorted(set(arr2))  # 先去重排序

        # 所谓的最少操作次数，实际上是要从arr1中找到一个最长严格递增子序列suba，把不在suba中的元素替换成arr2中的元素后，arr1是严格递增的，
        # 所以最少操作次数为 n - len(suba)
        # 记忆化搜索
        # 以dfs(i)表示以arr1[i]结尾的suba的长度，第i个元素没有被替换
        # 设j为arr1[i]左侧最近的没有被替换的元素位置，j < i，那么arr2中必须有足够多（至少i-j-1个）的元素处于(arr[j],arr[i])区间，否则不成立
        # dfs(i) = max(dfs(i), dfs(j) + 1) 条件满足时
        # 如果j=i-1，那么只要arr1[i-1] < arr1[i]，dfs(i) = max(dfs(i), dfs(i-1) + 1)
        # 如果j=-1，说明arr1的0到i-1的元素都要换掉，只要arr2中有足够多（至少i个）元素小于arr[i]，否则不成立
        # 对于不成立的情况，都可以初始化为-∞

        @cache
        def dfs(i: int) -> int:
            k = bisect_left(b, a[i])
            res = 0 if k >= i else -inf  # a[i]左侧元素全替换
            if i and a[i-1] < a[i]:
                res = max(res, dfs(i-1))
            for j in range(i-2, max(i-k-2, -1), -1):
                if b[k - (i-j-1)] > a[j]:
                    # a[j+1] 到 a[i-1] 替换成 b[k-(i-j-1)] 到 b[k-1]
                    res = max(res, dfs(j))

            return res + 1  # a[i]不替换，在这里 +1

        res = dfs(len(a) - 1)  # 最后添加的inf肯定是不用替换的，满足dfs的定义
        return -1 if res < 0 else len(a) - res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4]))  # 1
    print(solution.makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1]))  # 2
    print(solution.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3]))  # -1

#
# @lc app=leetcode.cn id=1439 lang=python3
#
# [1439] 有序矩阵中的第 k 个最小数组和
#
# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。

# 你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。


# 示例 1：
# 输入：mat = [[1, 3, 11], [2, 4, 6]], k = 5
# 输出：7
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1, 2], [1, 4], [3, 2], [3, 4], [1, 6]。其中第 5 个的和是 7 。

# 示例 2：
# 输入：mat = [[1, 3, 11], [2, 4, 6]], k = 9
# 输出：17

# 示例 3：
# 输入：mat = [[1, 10, 10], [1, 4, 5], [2, 3, 6]], k = 7
# 输出：9
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1, 1, 2], [1, 1, 3], [1, 4, 2], [1, 4, 3], [1, 1, 6], [1, 5, 2], [1, 5, 3]。其中第 7 个的和是 9 。

# 示例 4：
# 输入：mat = [[1, 1, 10], [2, 2, 9]], k = 7
# 输出：12


# 提示：
# m == mat.length
# n == mat.length[i]
# 1 <= m, n <= 40
# 1 <= k <= min(200, n ^ m)
# 1 <= mat[i][j] <= 5000
# mat[i] 是一个非递减数组

# Hard
# 复习


from typing import List
# @lc code=start
from heapq import heapify, heappop, heappush


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def combine(a1: List[int], a2: List[int]) -> List[int]:
            """
            取两个数组，数组和的前k个
            """
            if len(a1) < len(a2):
                return combine(a2, a1)  # 长的数组放前面

            hq = [(a1[0] + a2[i], 0, i) for i in range(len(a2))]
            heapify(hq)

            res = []
            limit = k
            while limit and hq:
                entry = heappop(hq)
                res.append(entry[0])
                if entry[1] + 1 < len(a1):
                    heappush(hq, (a1[entry[1] + 1] +
                             a2[entry[2]], entry[1] + 1, entry[2]))
                limit -= 1

            return res

        r = mat[0]
        for i in range(1, len(mat)):
            r = combine(r, mat[i])

        return r[-1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallest([[1, 3, 11], [2, 4, 6]], 5))  # 7
    print(solution.kthSmallest([[1, 3, 11], [2, 4, 6]], 9))  # 17
    print(solution.kthSmallest([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 7))  # 9
    print(solution.kthSmallest([[1, 1, 10], [2, 2, 9]], 7))  # 12

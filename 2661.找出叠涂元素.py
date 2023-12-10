#
# @lc app=leetcode.cn id=2661 lang=python3
#
# [2661] 找出叠涂元素
#
# 给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数。

# 从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。

# 请你找出 arr 中在 mat 的某一行或某一列上都被涂色且下标最小的元素，并返回其下标 i 。

# 示例 1：
# image explanation for example 1
# 输入：arr = [1,3,4,2], mat = [[1,4],[2,3]]
# 输出：2
# 解释：遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。

# 示例 2：
# image explanation for example 2
# 输入：arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
# 输出：3
# 解释：遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。
 

# 提示：
# m == mat.length
# n = mat[i].length
# arr.length == m * n
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# 1 <= arr[i], mat[r][c] <= m * n
# arr 中的所有整数 互不相同
# mat 中的所有整数 互不相同

from typing import List
# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        posMap = {}
        for r in range(m):
            for c in range(n):
                posMap[mat[r][c]] = (r, c)

        rowFlag = [0] * m
        colFlag = [0] * n
        for i, x in enumerate(arr):
            r, c = posMap[x]
            rowFlag[r] += 1
            colFlag[c] += 1
            if rowFlag[r] == n or colFlag[c] == m:
                return i
        return -1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstCompleteIndex([1,3,4,2], [[1,4],[2,3]])) # 2
    print(solution.firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]])) # 3
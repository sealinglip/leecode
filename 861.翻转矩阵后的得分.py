#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#
# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 
# 都更改为 0。

# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字
# 的总和。

# 返回尽可能高的分数。

# 示例：
# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 
# 提示：
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] 是 0 或 1

from typing import List
# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0]) # M行N列
        
        # 先将第一列都翻转成1开头
        for row in range(M):
            if A[row][0] == 0:
                for col in range(N):
                    A[row][col] = 1 - A[row][col]

        # 依次处理第2~N列，判断是否需要翻转
        total = M * (1 << (N - 1))
        for col in range(1, N):
            oneCnt = sum([A[row][col] for row in range(M)])
            if oneCnt < M - oneCnt:
                oneCnt = M - oneCnt # 需要翻转
            total += oneCnt * (1 << (N - col - 1))

        return total
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
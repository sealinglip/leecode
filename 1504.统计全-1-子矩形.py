#
# @lc app=leetcode.cn id=1504 lang=python3
#
# [1504] 统计全 1 子矩形
#
# https://leetcode.cn/problems/count-submatrices-with-all-ones/description/
#
# algorithms
# Medium (64.73%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    19.9K
# Total Submissions: 29.8K
# Testcase Example:  '[[1,0,1],[1,1,0],[1,1,0]]'
#
# 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。
# 
# 
# 示例 1：
# 输入：mat = [[1,0,1],[1,1,0],[1,1,0]]
# 输出：13
# 解释：
# 有 6 个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
# 
# 示例 2：
# 输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
# 
# 
# 提示：
# 1 <= m, n <= 150
# mat[i][j] 仅包含 0 或 1
# 
# 复习
#

from typing import List
# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # 方法1：
        # cnts = [[0] * n for _ in range(m)] # cnts[i][j]记录从位置(i,j)往左有连续多少个1
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if j == 0:
        #             cnts[i][j] = mat[i][j]
        #         elif mat[i][j] == 0:
        #             cnts[i][j] = 0
        #         else:
        #             cnts[i][j] = cnts[i][j-1] + 1

        #         tmp = j + 1
        #         for k in range(i, -1, -1):
        #             tmp = min(tmp, cnts[k][j])
        #             if tmp == 0:
        #                 break
        #             res += tmp

        # return res

        # 方法2：
        cnts = [0] * n # cnts[j]记录当前行第j列往上有连续多少个1
        res = 0
        for row in mat:
            for j in range(n):
                cnts[j] = 0 if row[j] == 0 else cnts[j] + 1
            st = [(-1, 0, -1)] # 栈里的每个元素代表(列索引, 以本行当前列为矩阵右角的全1矩阵个数, 本列往上连续的1的个数)
            for j, c in enumerate(cnts):
                while st[-1][2] >= c:
                    st.pop()
                k, prev, _ = st[-1]
                cur = prev + (j-k) * c
                st.append((j, cur, c))
                res += cur

        return res
            
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubmat([[1,0,1],[1,1,0],[1,1,0]])) # 13
    print(solution.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])) # 24

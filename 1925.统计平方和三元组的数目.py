#
# @lc app=leetcode.cn id=1925 lang=python3
#
# [1925] 统计平方和三元组的数目
#
# https://leetcode.cn/problems/count-square-sum-triples/description/
#
# algorithms
# Easy (69.33%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 30.4K
# Testcase Example:  '5'
#
# 一个 平方和三元组 (a,b,c) 指的是满足 a^2 + b^2 = c^2 的 整数 三元组 a，b 和 c 。
# 
# 给你一个整数 n ，请你返回满足 1 <= a, b, c <= n 的 平方和三元组 的数目。
# 
# 
# 示例 1：
# 输入：n = 5
# 输出：2
# 解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。
# 
# 示例 2：
# 输入：n = 10
# 输出：4
# 解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
# 
# 
# 提示：
# 1 <= n <= 250
# 
# 
#

# @lc code=start
from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n):
            for b in range(1, n):
                c = int(sqrt(a ** 2 + b ** 2 + 1))
                if c <= n and c ** 2 == a ** 2 + b ** 2:
                    res += 1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countTriples(5)) # 2
    print(solution.countTriples(10)) # 4

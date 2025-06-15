#
# @lc app=leetcode.cn id=2929 lang=python3
#
# [2929] 给小朋友们分糖果 II
#
# https://leetcode.cn/problems/distribute-candies-among-children-ii/description/
#
# algorithms
# Medium (41.96%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 22.5K
# Testcase Example:  '5\n2'
#
# 给你两个正整数 n 和 limit 。
# 请你将 n 颗糖果分给 3 位小朋友，确保没有任何小朋友得到超过 limit 颗糖果，请你返回满足此条件下的 总方案数 。
# 
# 
# 示例 1：
# 输入：n = 5, limit = 2
# 输出：3
# 解释：总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
# 
# 示例 2：
# 输入：n = 3, limit = 3
# 输出：10
# 解释：总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0,
# 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0)。
# 
# 
# 提示：
# 1 <= n <= 10^6
# 1 <= limit <= 10^6
# 
#

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            # 根据抽屉原理无解
            return 0
        # 设第一个小朋友拿i颗，那么 0 <= i <= min(n, limit)
        # 设第二个小朋友拿j颗，那么 0 <= j <= min(n-i, limit)，且 0 <= n-i-j <= limit（考虑第三个小朋友拿的数必须满足的条件）
        # n-i-j <= limit => n-i-limit <= j，所以有 max(0, n-i-limit) <= j
        # 即 max(0, n-i-limit) <= j <= min(n-i, limit)
        # 那么对任意的i，j的可选值个数为 max(0, min(n-i, limit) - max(0, n-i-limit) + 1)
        res = 0
        for i in range(min(n, limit)+1):
            res += max(0, min(n-i, limit) - max(0, n-i-limit) + 1)
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.distributeCandies(5, 2)) # 3
    print(solution.distributeCandies(3, 3)) # 10

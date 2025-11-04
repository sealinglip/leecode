#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#
# https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/description/
#
# algorithms
# Medium (60.79%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 40.8K
# Testcase Example:  '"abaac"\n[1,2,3,4,5]'
#
# Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。
# 
# Alice 想要把绳子装扮成 五颜六色的 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成
# 彩色 。给你一个 下标从 0 开始 的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i
# 个气球需要的时间（以秒为单位）。
# 
# 返回 Bob 使绳子变成 彩色 需要的 最少时间 。
# 
# 
# 示例 1：
# 输入：colors = "abaac", neededTime = [1,2,3,4,5]
# 输出：3
# 解释：在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。
# Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
# 移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。
# 
# 示例 2：
# 输入：colors = "abc", neededTime = [1,2,3]
# 输出：0
# 解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。
# 
# 示例 3：
# 输入：colors = "aabaa", neededTime = [1,2,3,4,1]
# 输出：2
# 解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
# 移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。
# 
# 
# 提示：
# n == colors.length == neededTime.length
# 1 <= n <= 10^5
# 1 <= neededTime[i] <= 10^4
# colors 仅由小写英文字母组成
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # 连续相同颜色的气球，只能留下一个移除时间最高的
        cnt = total = ma = res = 0
        prevColor = ''
        for c, t in zip(colors, neededTime):
            if c == prevColor:
                cnt += 1
                total += t
                ma = max(ma, t)
            else:
                if cnt > 1:
                    res += total - ma
                cnt = 1
                total = ma = t
            prevColor = c

        if cnt > 1:
            res += total - ma

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCost("abaac", [1,2,3,4,5])) # 3
    print(solution.minCost("abc", [1,2,3])) # 0
    print(solution.minCost("aabaa", [1,2,3,4,1])) # 2

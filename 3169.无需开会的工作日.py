#
# @lc app=leetcode.cn id=3169 lang=python3
#
# [3169] 无需开会的工作日
#
# https://leetcode.cn/problems/count-days-without-meetings/description/
#
# algorithms
# Medium (39.18%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 24.5K
# Testcase Example:  '10\n[[5,7],[1,3],[9,10]]'
#
# 给你一个正整数 days，表示员工可工作的总天数（从第 1 天开始）。另给你一个二维数组 meetings，长度为 n，其中 meetings[i] =
# [start_i, end_i] 表示第 i 次会议的开始和结束天数（包含首尾）。
# 
# 返回员工可工作且没有安排会议的天数。
# 
# 注意：会议时间可能会有重叠。
# 
# 
# 示例 1：
# 输入：days = 10, meetings = [[5,7],[1,3],[9,10]]
# 输出：2
# 解释：
# 第 4 天和第 8 天没有安排会议。
# 
# 示例 2：
# 输入：days = 5, meetings = [[2,4],[1,3]]
# 输出：1
# 解释：
# 第 5 天没有安排会议。
# 
# 示例 3：
# 输入：days = 6, meetings = [[1,6]]
# 输出：0
# 解释：
# 所有工作日都安排了会议。
# 
# 
# 提示：
# 1 <= days <= 10^9
# 1 <= meetings.length <= 10^5
# meetings[i].length == 2
# 1 <= meetings[i][0] <= meetings[i][1] <= days
# 
#

from typing import List
# @lc code=start
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        meetings.sort(key=lambda e: (e[0], -e[1])) # 按开始时间升序、结束时间降序排列
        prevEnd = 0
        for s, e in meetings:
            if s > prevEnd:
                res += s - prevEnd - 1
            if e > prevEnd:
                prevEnd = e
        res += days - prevEnd
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countDays(10, [[5,7],[1,3],[9,10]])) # 2
    print(solution.countDays(5, [[2,4],[1,3]])) # 1
    print(solution.countDays(6, [[1,6]])) # 0
    
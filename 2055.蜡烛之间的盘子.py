#
# @lc app=leetcode.cn id=2055 lang=python3
#
# [2055] 蜡烛之间的盘子
#
# 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，
# 其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

# 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示
# 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间
# 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

# 比方说，s = "||**||**|*" ，查询[3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，
# 子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
# 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。


# 示例 1:
# 输入：s = "**|**|***|", queries = [[2, 5], [5, 9]]
# 输出：[2, 3]
# 解释：
# - queries[0] 有两个盘子在蜡烛之间。
# - queries[1] 有三个盘子在蜡烛之间。

# 示例 2:
# 输入：s = "***|**|*****|**||**|*", queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
# 输出：[9, 0, 0, 0, 0]
# 解释：
# - queries[0] 有 9 个盘子在蜡烛之间。
# - 另一个查询没有盘子在蜡烛之间。


# 提示：
# 3 <= s.length <= 10^5
# s 只包含字符 '*' 和 '|' 。
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= lefti <= righti < s.length


import enum
from typing import List
# @lc code=start


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # 遍历蜡烛的位置，建立速查表
        # left[i]表示第i个位置，其左边（含自身）第一根蜡烛的位置
        # right[i]表示第i个位置，其右边（含自身）第一根蜡烛的位置
        left = [0] * n
        preSum = [0] * n
        l, cnt = -1, 0
        for i, c in enumerate(s):
            if c == '|':
                l = i
            else:
                cnt += 1
            preSum[i] = cnt
            left[i] = l

        right = [0] * n
        r = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        res = []
        for x, y in queries:
            l = right[x]
            r = left[y]
            res.append(preSum[r] - preSum[l] if (l >=
                                                 0 and r >= 0 and l < r) else 0)
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.platesBetweenCandles(
        "**|**|***|", [[2, 5], [5, 9]]))  # [2, 3]
    print(solution.platesBetweenCandles(
        "***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))  # [9, 0, 0, 0, 0]

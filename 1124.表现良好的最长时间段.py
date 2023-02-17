#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。

# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。

# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。

# 请你返回「表现良好时间段」的最大长度。


# 示例 1：
# 输入：hours = [9, 9, 6, 0, 6, 6, 9]
# 输出：3
# 解释：最长的表现良好时间段是[9, 9, 6]。

# 示例 2：
# 输入：hours = [6, 6, 6]
# 输出：0


# 提示：
# 1 <= hours.length <= 10^4
# 0 <= hours[i] <= 16

# 复习

# from itertools import accumulate
from typing import List
# @lc code=start


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 下面的不够简洁
        # # 求出劳累天-摸鱼天差值的前缀和
        # delta = list(accumulate(1 if h > 8 else -1 for h in hours))
        # #
        # map = {0: [-1, -1]}
        # for i, d in enumerate(delta):
        #     if d not in map:
        #         map[d] = [i, i]
        #     else:
        #         map[d][1] = i

        # # 处理最大跨度
        # ks = sorted(map.keys())
        # res = max([max(map[k][1] for k in ks[i+1:]) - map[ks[i]][0]
        #            for i in range(len(ks) - 1)], default=0)
        # return max(res, 0)

        # 优化版
        d = {}
        res = accum = 0
        for i, h in enumerate(hours):
            accum += 1 if h > 8 else -1
            if accum > 0:
                res = max(res, i + 1)
            else:
                if (accum - 1) in d:
                    res = max(res, i - d[accum - 1])
                if accum not in d:
                    d[accum] = i

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestWPI([9, 9, 6, 0, 6, 6, 9]))  # 3
    print(solution.longestWPI([6, 6, 6]))  # 0
    print(solution.longestWPI([9, 9, 9]))  # 3

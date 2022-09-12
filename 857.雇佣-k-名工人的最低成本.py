#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#
# 有 n 名工人。 给定两个数组 quality 和 wage ，其中，quality[i] 表示第 i 名工人的工作质量，其最低期望工资为 wage[i]。

# 现在我们想雇佣 k 名工人组成一个工资组。在雇佣 一组 k 名工人时，我们必须按照下述规则向他们支付工资：

# 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
# 工资组中的每名工人至少应当得到他们的最低期望工资。
# 给定整数 k ，返回 组成满足上述条件的付费群体所需的最小金额 。在实际答案的 10^-5 以内的答案将被接受。


# 示例 1：
# 输入： quality = [10, 20, 5], wage = [70, 50, 30], k = 2
# 输出： 105.00000
# 解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。

# 示例 2：
# 输入： quality = [3, 1, 10, 10, 1], wage = [4, 8, 2, 2, 7], k = 3
# 输出： 30.66667
# 解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。


# 提示：
# n == quality.length == wage.length
# 1 <= k <= n <= 10^4
# 1 <= quality[i], wage[i] <= 10^4

# Hard
# 复习

from typing import List
import heapq
# @lc code=start


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(zip(quality, wage),
                         key=lambda w: w[1] / w[0])  # 按工人单位产值排序
        hq = []
        qsum = 0
        res = float('inf')
        for q, w in workers:
            heapq.heappush(hq, -q)
            qsum += q
            if len(hq) > k:
                qsum += heapq.heappop(hq)
            if len(hq) == k:
                res = min(res, qsum * w / q)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.mincostToHireWorkers(
        [10, 20, 5], [70, 50, 30], 2))  # 105.00000
    print(solution.mincostToHireWorkers(
        [3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))  # 30.66667

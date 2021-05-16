#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
# 返回分配方案中尽可能 最小 的 最大工作时间 。


# 示例 1：
# 输入：jobs = [3, 2, 3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。

# 示例 2：
# 输入：jobs = [1, 2, 4, 7, 8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。


# 提示：
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 10^7

from typing import List
# @lc code=start


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 贪心求一个次优解
        from heapq import heapify, heappush, heappop
        heap = [0]*k
        heapify(heap)
        jobs = sorted(jobs)[::-1]
        for i in jobs:
            heappush(heap, heappop(heap)+i)
        m = max(heap)

        a = [0]*k  # k 个工人，每个工人的工作量，初始为 0

        def job(j):
            nonlocal m
            if j == len(jobs):
                m = min(m, max(a))  # 记录已知最优解
                return
            for i in range(min(k, j+1)):  # 剪枝，第 j 个工作只能分配给前 j 个工人
                if a[i]+jobs[j] > m:  # 如果工作 j 分配给工人 i 后，工人 i 工作量大于已知最优解 m ，跳过
                    continue
                a[i] += jobs[j]
                job(j+1)
                a[i] -= jobs[j]
        job(0)
        return m

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTimeRequired([3, 2, 3], 3))
    print(solution.minimumTimeRequired([8, 7, 5, 5, 5], 2))
    print(solution.minimumTimeRequired([1, 2, 4, 7, 8], 2))

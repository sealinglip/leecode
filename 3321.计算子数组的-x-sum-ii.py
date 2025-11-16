#
# @lc app=leetcode.cn id=3321 lang=python3
#
# [3321] 计算子数组的 x-sum II
#
# https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-ii/description/
#
# algorithms
# Hard (29.42%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 10.3K
# Testcase Example:  '[1,1,2,2,3,4,2,3]\n6\n2'
#
# 给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。
# 
# 数组的 x-sum 计算按照以下步骤进行：
# 
# 统计数组中所有元素的出现次数。
# 仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
# 计算结果数组的和。
# 
# 注意，如果数组中的不同元素少于 x 个，则其 x-sum 是数组的元素总和。
# 
# 返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的
# x-sum。
# 
# 子数组 是数组内的一个连续 非空 的元素序列。
# 
# 
# 示例 1：
# 输入：nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
# 输出：[6,10,12]
# 解释：
# 对于子数组 [1, 1, 2, 2, 3, 4]，只保留元素 1 和 2。因此，answer[0] = 1 + 1 + 2 + 2。
# 对于子数组 [1, 2, 2, 3, 4, 2]，只保留元素 2 和 4。因此，answer[1] = 2 + 2 + 2 + 4。注意 4
# 被保留是因为其数值大于出现其他出现次数相同的元素（3 和 1）。
# 对于子数组 [2, 2, 3, 4, 2, 3]，只保留元素 2 和 3。因此，answer[2] = 2 + 2 + 2 + 3 + 3。
# 
# 示例 2：
# 输入：nums = [3,8,7,8,7,5], k = 2, x = 2
# 输出：[11,15,15,15,12]
# 解释：
# 由于 k == x，answer[i] 等于子数组 nums[i..i + k - 1] 的总和。
# 
# 
# 提示：
# nums.length == n
# 1 <= n <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= x <= k <= nums.length
# 
# 
#


from collections import Counter
from typing import List

from sortedcontainers import SortedList
# @lc code=start
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        cnt = Counter(nums[:k])
        topX = SortedList((c, v) for v, c in cnt.most_common())
        rest = SortedList()

        sumX = sum(c * v for c, v in topX)

        def rebalance() -> None:
            nonlocal sumX
            # 只保留最多的x个
            while len(topX) > x:
                p = topX[0]
                rest.add(p)
                topX.remove(p)
                sumX -= p[0] * p[1]
            while len(topX) < x and rest:
                p = rest[-1]
                topX.add(p)
                rest.remove(p)
                sumX += p[0] * p[1]

        rebalance()
        

        res = [sumX]

        def increase(v: int) -> None:
            nonlocal sumX
            c = cnt[v]
            cnt[v] += 1
            p = (c, v)
            if p in topX:
                topX.remove(p)
                topX.add((c+1, v))
                sumX += v
            else:
                if p in rest:
                    rest.remove(p)
                p = (c+1, v)
                if topX and p > topX[0]:
                    topX.add(p)
                    sumX += p[0] * p[1]
                else:
                    rest.add(p)

        def decrease(v: int) -> None:
            nonlocal sumX
            c = cnt[v]
            cnt[v] -= 1
            p = (c, v)
            if p in rest:
                rest.remove(p)
                rest.add((c-1, v))
            else:
                topX.remove(p)
                p = (c-1, v)
                if topX and p > topX[0]:
                    topX.add(p)
                    sumX -= v
                else:
                    rest.add(p)
                    sumX -= c * v

        for i in range(n - k):
            # 一出一进更新 topX 和 sumX
            _out = nums[i]
            _in = nums[i+k]
            if _in != _out:
                increase(_in)
                decrease(_out)
                rebalance()
            res.append(sumX)

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findXSum([7,4,10,3,5], 1, 1)) # [7,4,10,3,5]
    print(solution.findXSum([1,1,2,2,3,4,2,3], 6, 2)) # [6,10,12]
    print(solution.findXSum([3,8,7,8,7,5], 2, 2)) # [11,15,15,15,12]
    
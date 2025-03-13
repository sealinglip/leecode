#
# @lc app=leetcode.cn id=2234 lang=python3
#
# [2234] 花园的最大总美丽值
#
# Alice 是 n 个花园的园丁，她想通过种花，最大化她所有花园的总美丽值。

# 给你一个下标从 0 开始大小为 n 的整数数组 flowers ，其中 flowers[i] 是第 i 个花园里已经种的花的数目。已经种了的花 不能 移走。同时给你 newFlowers ，表示 Alice 额外可以种花的 最大数目 。同时给你的还有整数 target ，full 和 partial 。

# 如果一个花园有 至少 target 朵花，那么这个花园称为 完善的 ，花园的 总美丽值 为以下分数之 和 ：

# 完善 花园数目乘以 full.
# 剩余 不完善 花园里，花的 最少数目 乘以 partial 。如果没有不完善花园，那么这一部分的值为 0 。
# 请你返回 Alice 种最多 newFlowers 朵花以后，能得到的 最大 总美丽值。


# 示例 1：
# 输入：flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
# 输出：14
# 解释：Alice 可以按以下方案种花
# - 在第 0 个花园种 2 朵花
# - 在第 1 个花园种 3 朵花
# - 在第 2 个花园种 1 朵花
# - 在第 3 个花园种 1 朵花
# 花园里花的数目为 [3,6,2,2] 。总共种了 2 + 3 + 1 + 1 = 7 朵花。
# 只有 1 个花园是完善的。
# 不完善花园里花的最少数目是 2 。
# 所以总美丽值为 1 * 12 + 2 * 1 = 12 + 2 = 14 。
# 没有其他方案可以让花园总美丽值超过 14 。

# 示例 2：
# 输入：flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
# 输出：30
# 解释：Alice 可以按以下方案种花
# - 在第 0 个花园种 3 朵花
# - 在第 1 个花园种 0 朵花
# - 在第 2 个花园种 0 朵花
# - 在第 3 个花园种 2 朵花
# 花园里花的数目为 [5,4,5,5] 。总共种了 3 + 0 + 0 + 2 = 5 朵花。
# 有 3 个花园是完善的。
# 不完善花园里花的最少数目为 4 。
# 所以总美丽值为 3 * 2 + 4 * 6 = 6 + 24 = 30 。
# 没有其他方案可以让花园总美丽值超过 30 。
# 注意，Alice可以让所有花园都变成完善的，但这样她的总美丽值反而更小。
 

# 提示：
# 1 <= flowers.length <= 10^5
# 1 <= flowers[i], target <= 10^5
# 1 <= newFlowers <= 10^10
# 1 <= full, partial <= 10^5

# Hard


from itertools import accumulate
from typing import List
# @lc code=start
from bisect import bisect
class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)

        # 因为full和partial的设置不确定，所以不一定完善花园数目越多越好
        # 假定最后搞出k个完善花园，那肯定从多到少去种合适，这样可以剩余最多可用的去填谷拉伸不完善里的最低值
        flowers.sort(reverse=True)
        preSum = [0] + list(accumulate(0 if f >= target else target - f for f in flowers)) # preSum[i]为搞出i个完善花园需要的花数
        postSum = [0] + list(accumulate((flowers[i-1] - flowers[i]) * (n-i) for i in range(n-1, 0, -1)))# 从后向前填平需要的花数，postSum[i]为flowers[n-i-1:]全搞成flowers[n-i-1]这么多需要的花数
        
        def beauty(k: int) -> int:
            """
            搞出k个完善花园能获得的最大魅力值，如果搞不出来返回0
            """
            if newFlowers < preSum[k]:
                return 0
            value = k * full
            if k < n:
                # 还有不完善的花园
                rest = newFlowers - preSum[k] # 搞出k个完善花园后剩下的花
                i = bisect(postSum, rest) # 剩下的花能填平到最少的i个花园，i一定大于0
                if k + i >= n: # 剩的不完善花园数都不到i个了
                    i = n - k
                rest -= postSum[i-1]
                minPartial = flowers[n-i]
                if rest > 0:
                    minPartial += rest // i
                value += min(target-1, minPartial) * partial
            return value
        
        minK = bisect(preSum, 0) - 1
        maxK = min(bisect(preSum, newFlowers), n) # 最多搞出这么多个完善花园
        # 我们实际上要找max(beauty(i) for i in range(maxK+1))，但beauty(i)不是一个单调函数，所以不能用区间边界的值
        return max(beauty(i) for i in range(minK, maxK+1))
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([10] * 9 + [9], 10, 10, 10, 10)) # 180
    print(solution.maximumBeauty([100000] * 100000, 100000, 100000, 100000, 100000)) # 10000000000
    print(solution.maximumBeauty([100000] * 99999 + [99999], 100000, 100000, 100000, 100000)) # 19999800000
    print(solution.maximumBeauty([22323,64818,97718,14354,27837,6347,43299,23010,18590,12706,1579,52401,23473,82978,1012,2248,50247,755,12672,57870,90646,87848,71069,82723,83385,66909,39266,97768,62453,30454,68978,88590,11213,74010,65683,75460,3118,98281,28128,84992,52206,92770,74240,33266,41603,19267,36991,86658,43834,84533,75187,31502,61181,31333,37324,13352,51735,89812,56745,44204,85482,70358,48830,91989,82778,34042,3293,63626,41301,43763,39681,91917,40165,57944,34357,22395,26084,21666,40781,28998,12385,10720,66853,42324,28327,30125,15522,12223], 997843, 100000, 4880, 45790)) # 2080606020
    print(solution.maximumBeauty([1,3,1,1], 7, 6, 12, 1)) # 14
    print(solution.maximumBeauty([2,4,5,3], 10, 5, 2, 6)) # 30

# 给你一个整数数组 rewardValues，长度为 n，代表奖励的值。

# 最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：

# 从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
# 如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。
# 以整数形式返回执行最优操作能够获得的 最大 总奖励。


# 示例 1：
# 输入：rewardValues = [1,1,3,3]
# 输出：4
# 解释：
# 依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。

# 示例 2：
# 输入：rewardValues = [1,6,4,3,2]
# 输出：11
# 解释：
# 依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。


# 提示：
# 1 <= rewardValues.length <= 2000
# 1 <= rewardValues[i] <= 2000

# 复习

# from functools import cache
from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        n = len(rewardValues)

        # 不出所料，下面的解法会TLE
        # rewardValues.sort(reverse=True)
        # @cache
        # def maxReward(fromIdx: int, limit: int) -> int:
        #     '''
        #     从降序排列后的rewardValues[fromIdx:]中选择元素，其总和不能达到或超过limit时能达到的最大值
        #     '''
        #     while fromIdx < n and rewardValues[fromIdx] >= limit:
        #         fromIdx += 1
        #     if fromIdx == n:
        #         return 0
        #     else:
        #         return max(rewardValues[fromIdx] + maxReward(fromIdx+1, min(rewardValues[fromIdx], limit - rewardValues[fromIdx])), maxReward(fromIdx+1, limit))
        
        # return maxReward(0, (rewardValues[0] << 1))
        rewardValues.sort()
        flag = [0] * ((rewardValues[-1] << 1)) # flag标记某奖励能否获取到
        flag[0] = 1
        for r in rewardValues:
            for i in range(r):
                if flag[i]:
                    flag[i+r] = 1
        res = 0
        for i in range(len(flag) - 1, -1, -1):
            if flag[i]:
                res = i
                break
        return res
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTotalReward([1,1,3,3])) # 4
    print(solution.maxTotalReward([1,6,4,3,2])) # 11
    print(solution.maxTotalReward([9,6,5,3,2,1])) # 17

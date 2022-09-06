#
# @lc app=leetcode.cn id=1224 lang=python3
#
# [1224] 最大相等频率
#
# 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：

# 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。


# 示例 1：
# 输入：nums = [2, 2, 1, 1, 5, 3, 3, 5]
# 输出：7
# 解释：对于长度为 7 的子数组[2, 2, 1, 1, 5, 3, 3]，如果我们从中删去 nums[4] = 5，就可以得到[2, 2, 1, 1, 3, 3]，里面每个数字都出现了两次。

# 示例 2：
# 输入：nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
# 输出：13


# 提示：
# 2 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5

# 复习
# Hard

from typing import List
from collections import Counter
# @lc code=start


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # 下面的方法会TLE
        res = 1  # 至少为1
        # cnt = Counter()
        # once = set()  # 记录只出现一次的数字
        # times = 0  # 记录其他数字出现的次数
        # maxOccur = None
        # for i, n in enumerate(nums):
        #     cnt[n] += 1
        #     curTimes = cnt[n]
        #     if curTimes == 1:
        #         once.add(n)
        #     elif curTimes == 2:
        #         once.remove(n)

        #     if curTimes > times:
        #         times = curTimes
        #         maxOccur = n

        #     if len(once) == 1 or times == 1:
        #         # 有一个单个的数字
        #         if n in once or curTimes == times:
        #             # 判断是否其他数字都是等次
        #             if all([cnt[c] == times for c in cnt.keys() if c not in once]):
        #                 res = i + 1
        #     else:
        #         # 判断是不是有一个数字比其他数字多一个
        #         if curTimes == times:
        #             if all([cnt[c] == times - 1 for c in cnt.keys() if c != n]):
        #                 res = i + 1
        #         elif curTimes == times - 1:
        #             if all([cnt[c] == curTimes for c in cnt.keys() if c != maxOccur]):
        #                 res = i + 1

        cnt = Counter()  # 记录每个字母的出现次数
        freq = Counter()  # 记录每个出现次数的字母数
        maxFreq = 0  # 最大出现次数
        for i, n in enumerate(nums):
            if cnt[n]:
                freq[cnt[n]] -= 1
            cnt[n] += 1
            freq[cnt[n]] += 1
            maxFreq = max(cnt[n], maxFreq)

            if maxFreq == 1\
                    or (maxFreq + (maxFreq - 1) * freq[maxFreq - 1] == i + 1 and freq[maxFreq] == 1)\
                    or (maxFreq * freq[maxFreq] + 1 == i + 1 and freq[1] == 1):
                res = max(res, i + 1)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEqualFreq([10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]))  # 8
    print(solution.maxEqualFreq([1, 1, 1, 2, 2, 2]))  # 5
    print(solution.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5]))  # 7
    print(solution.maxEqualFreq([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]))  # 13

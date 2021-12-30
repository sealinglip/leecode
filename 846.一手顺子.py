#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#
# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。
# 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。


# 示例 1：
# 输入：hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
# 输出：true
# 解释：Alice 手中的牌可以被重新排列为[1, 2, 3]，[2, 3, 4]，[6, 7, 8]。

# 示例 2：
# 输入：hand = [1, 2, 3, 4, 5], groupSize = 4
# 输出：false
# 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。


# 提示：
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length

from typing import List
# @lc code=start
from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            # 不能整除的情况
            return False

        cnt = Counter(hand)
        hq = list(cnt.keys())
        hq.sort()  # 排序
        while hq:
            start = hq[0]
            c = cnt[start]
            if c > 0:
                # 抽取一个序列
                for i in range(start, start + groupSize):
                    if cnt[i] > 0:
                        cnt[i] -= 1
                    else:
                        return False
            else:
                heapq.heappop(hq)

        return True


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isNStraightHand([8, 10, 12], 3))  # False
    print(solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))  # True
    print(solution.isNStraightHand([1, 2, 3, 4, 5], 4))  # False

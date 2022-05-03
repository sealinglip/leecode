#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#
# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

# 每一步，你可以从下标 i 跳到下标：

# i + 1 满足：i + 1 < arr.length
# i - 1 满足：i - 1 >= 0
# j 满足：arr[i] == arr[j] 且 i != j
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。

# 注意：任何时候你都不能跳到数组外面。


# 示例 1：
# 输入：arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 - -> 4 - -> 3 - -> 9 。下标 9 为数组的最后一个元素的下标。

# 示例 2：
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。

# 示例 3：
# 输入：arr = [7, 6, 9, 6, 9, 6, 9, 7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。

# 示例 4：
# 输入：arr = [6, 1, 9]
# 输出：2

# 示例 5：
# 输入：arr = [11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]
# 输出：3


# 提示：
# 1 <= arr.length <= 5 * 10 ^ 4
# -10 ^ 8 <= arr[i] <= 10 ^ 8

# Hard

from typing import List
# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 0:
            return 0

        # 下面这个解法会TLE
        # 关键就在于下面的：del distri[arr[i]]
        # 加上这个可以去掉很多重复判断
        distri = defaultdict(list)
        for i, e in enumerate(arr):
            distri[e].append(i)  # 记录下数字出现的位置

        distFromStart = {0: 0}  # 从起点出发搜索
        queueFromStart = deque([(0, 0)])
        distFromEnd = {N - 1: 0}  # 从终点出发搜索
        queueFromEnd = deque([(N - 1, 0)])

        while queueFromStart and queueFromEnd:
            i, s = queueFromStart[0]
            if i == N - 1:
                return s
            while queueFromStart and queueFromStart[0][1] == s:  # 以步数相同为一层，按层出
                i = queueFromStart.popleft()[0]
                if i > 0 and (i - 1) not in distFromStart:
                    if i - 1 in distFromEnd:
                        return s + 1 + distFromEnd[i - 1]
                    queueFromStart.append((i - 1, s + 1))
                    distFromStart[i - 1] = s + 1
                if i < N - 1 and i + 1 not in distFromStart:
                    if i + 1 in distFromEnd:
                        return s + 1 + distFromEnd[i + 1]
                    queueFromStart.append((i + 1, s + 1))
                    distFromStart[i + 1] = s + 1
                for d in distri[arr[i]]:
                    if d != i and d not in distFromStart:
                        if d in distFromEnd:
                            return s + 1 + distFromEnd[d]
                        queueFromStart.append((d, s + 1))
                        distFromStart[d] = s + 1
                del distri[arr[i]]

            i, s = queueFromEnd[0]
            if i == 0:
                return s
            while queueFromEnd and queueFromEnd[0][1] == s:
                i = queueFromEnd.popleft()[0]
                if i > 0 and (i - 1) not in distFromEnd:
                    if i - 1 in distFromStart:
                        return s + 1 + distFromStart[i - 1]
                    queueFromEnd.append((i - 1, s + 1))
                    distFromEnd[i - 1] = s + 1
                if i < N - 1 and i + 1 not in distFromEnd:
                    if i + 1 in distFromStart:
                        return s + 1 + distFromStart[i + 1]
                    queueFromEnd.append((i + 1, s + 1))
                    distFromEnd[i + 1] = s + 1
                for d in distri[arr[i]]:
                    if d != i and d not in distFromEnd:
                        if d in distFromStart:
                            return s + 1 + distFromStart[d]
                        queueFromEnd.append((d, s + 1))
                        distFromEnd[d] = s + 1
                del distri[arr[i]]

        return N - 1  # 最多一步一步从起点挪到终点


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minJumps(
        [7] * 10000 + [8] * 30000 + [9] * 10000))  # 5
    print(solution.minJumps(
        [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))  # 3
    print(solution.minJumps([7]))  # 0
    print(solution.minJumps([7, 6, 9, 6, 9, 6, 9, 7]))  # 1
    print(solution.minJumps([6, 1, 9]))  # 2
    print(solution.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))  # 3

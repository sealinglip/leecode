#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#
# 给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。
# 子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。


# 示例 1：
# 输入：arr = [1, 2, 3, 4], difference = 1
# 输出：4
# 解释：最长的等差子序列是[1, 2, 3, 4]。

# 示例 2：
# 输入：arr = [1, 3, 5, 7], difference = 1
# 输出：1
# 解释：最长的等差子序列是任意单个元素。

# 示例 3：
# 输入：arr = [1, 5, 7, 8, 5, 3, 4, 2, 1], difference = -2
# 输出：4
# 解释：最长的等差子序列是[7, 5, 3, 1]。


# 提示：
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i], difference <= 10^4


from typing import List
# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # # 👇的解法会超时
        # if difference == 0:
        #     # difference 为0 特殊处理
        #     cnt = Counter(arr)
        #     return cnt.most_common(1)[0][1]

        # map = defaultdict(list)  # key为数字，value为位置列表（升序）
        # for i, n in enumerate(arr):
        #     map[n].append(i)
        # N = len(arr)
        # visited = [False] * N
        # longest = 0

        # for i in range(N):
        #     if not visited[i]:
        #         l, pos = 1, i
        #         num = arr[pos] + difference
        #         visited[i] = True
        #         while num in map:
        #             # 判断num的位置有在pos之后的
        #             for p in map[num]:
        #                 if p > pos:
        #                     pos = p
        #                     break
        #             else:
        #                 # 没有找到合适的下一个数
        #                 break
        #             num += difference
        #             visited[pos] = True
        #             l += 1
        #         if l > longest:
        #             longest = l

        # return longest

        # 动态规划
        dp = defaultdict(int)
        # 记dp[num]为以当前位置的num结尾的最长子序列长度
        # 在遍历过程中，同一个数字对应的dp是会变化的（如果数组中有重复数字）
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubsequence(
        [4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8], 0))  # 2
    print(solution.longestSubsequence([1, 2, 3, 4], 1))  # 4
    print(solution.longestSubsequence([1, 2, 3, 4], 1))  # 4
    print(solution.longestSubsequence([1, 3, 5, 7], 1))  # 1
    print(solution.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))  # 4

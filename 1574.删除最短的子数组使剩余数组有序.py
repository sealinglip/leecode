#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#
# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

# 一个子数组指的是原数组中连续的一个子序列。

# 请你返回满足题目要求的最短子数组的长度。


# 示例 1：
# 输入：arr = [1, 2, 3, 10, 4, 2, 3, 5]
# 输出：3
# 解释：我们需要删除的最短子数组是[10, 4, 2] ，长度为 3 。剩余元素形成非递减数组[1, 2, 3, 3, 5] 。
# 另一个正确的解为删除子数组[3, 10, 4] 。

# 示例 2：
# 输入：arr = [5, 4, 3, 2, 1]
# 输出：4
# 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除[5, 4, 3, 2]，要么删除[4, 3, 2, 1]。

# 示例 3：
# 输入：arr = [1, 2, 3]
# 输出：0
# 解释：数组已经是非递减的了，我们不需要删除任何元素。

# 示例 4：
# 输入：arr = [1]
# 输出：0


# 提示：
# 1 <= arr.length <= 10 ^ 5
# 0 <= arr[i] <= 10 ^ 9

# 复习

from typing import List
# @lc code=start


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 子数组要求连续
        # 所以理论上就是将原数组切分成三个部分（首尾都可以为空），首尾部分必须是非单调递减（如果非空的话），首尾连接起来也是非递减
        n = len(arr)
        l = 0
        while l < n-1 and arr[l] <= arr[l+1]:
            l += 1
        #  下面的实现不够简单
        # r = n - 1
        # while r > 0 and arr[r] >= arr[r-1]:
        #     r -= 1

        # if l >= r:
        #     return 0
        # elif arr[r] >= arr[l]:
        #     # 只要把中间的元素去掉即可
        #     return r - l - 1
        # lm = l  # 打标记
        # while l >= 0 and arr[l] > arr[r]:
        #     l -= 1
        # span = r - l - 1
        # while r < n and arr[r] < arr[lm]:
        #     while l < lm and arr[l+1] <= arr[r]:
        #         l += 1
        #     span = min(span, r - l - 1)
        #     r += 1
        # span = min(span, r - lm - 1)
        # return span
        if l == n - 1:
            return 0
        span = n - l - 1
        for r in range(n-1, l, -1):
            while l >= 0 and arr[l] > arr[r]:
                l -= 1
            span = min(span, r - l - 1)
            if arr[r-1] > arr[r]:
                break
        return span


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLengthOfShortestSubarray(
        [1, 2, 3, 10, 0, 7, 8, 9]))  # 2
    print(solution.findLengthOfShortestSubarray(
        [1, 2, 3, 10, 4, 2, 3, 5]))  # 3
    print(solution.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))  # 4
    print(solution.findLengthOfShortestSubarray([1, 2, 3]))  # 0
    print(solution.findLengthOfShortestSubarray([1]))  # 0

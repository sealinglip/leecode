#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

# 示例 1：
# 输入：arr = [0, 1, 0]
# 输出：1

# 示例 2：
# 输入：arr = [0, 2, 1, 0]
# 输出：1

# 示例 3：
# 输入：arr = [0, 10, 5, 2]
# 输出：1

# 示例 4：
# 输入：arr = [3, 4, 5, 1]
# 输出：2

# 示例 5：
# 输入：arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
# 输出：2

# 提示：
# 3 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^6
# 题目数据保证 arr 是一个山脉数组

from typing import List
# @lc code=start


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr) - 1
        lo, hi = 0, N

        while lo < hi:
            mid = (hi + lo) >> 1
            if 0 < mid < N:
                if arr[mid - 1] < arr[mid]:
                    if arr[mid] > arr[mid + 1]:
                        return mid
                    else:
                        lo = mid + 1
                else:
                    hi = mid - 1
            else:
                return lo if mid == hi else hi
        return lo

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.peakIndexInMountainArray([3, 5, 3, 2, 0]))
    print(solution.peakIndexInMountainArray(
        [18, 29, 38, 59, 98, 100, 99, 98, 90]))

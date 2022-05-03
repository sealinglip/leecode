#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#
# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

# 例如：
# [2, 3, 4]，中位数是 3
# [2, 3]，中位数是(2 + 3) / 2 = 2.5
# 给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
# 你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。


# 示例：
# 给出 nums = [1, 3, -1, -3, 5, 3, 6, 7]，以及 k = 3。

# 窗口位置                      中位数
# ---------------              -----
# [1  3  -1] -3  5  3  6  7     1
#  1 [3  -1  -3] 5  3  6  7    -1
#  1  3 [-1  -3  5] 3  6  7    -1
#  1  3  -1 [-3  5  3] 6  7     3
#  1  3  -1  -3 [5  3  6] 7     5
#  1  3  -1  -3  5 [3  6  7]    6
# 因此，返回该滑动窗口的中位数数组[1, -1, -1, 3, 5, 6]。


# 提示：
# 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
# 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。

# Hard

from typing import List
# @lc code=start


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return []
        N = len(nums)
        if k > N:
            return []

        mid = k >> 1  # 中位数索引
        odd = k & 1  # 是否奇数
        window = nums[:k]
        res = []
        for i in range(N - k + 1):
            window.sort()
            if odd:
                res.append(window[mid])
            else:
                res.append((window[mid] + window[mid - 1]) / 2)
            if i < N - k:
                window.remove(nums[i])
                window.append(nums[i + k])

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.medianSlidingWindow([1, 4, 2, 3], 4))
    print(solution.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

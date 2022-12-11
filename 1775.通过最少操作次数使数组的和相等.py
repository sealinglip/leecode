#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#
# 给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。

# 每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。

# 请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 - 1 。


# 示例 1：
# 输入：nums1 = [1, 2, 3, 4, 5, 6], nums2 = [1, 1, 2, 2, 2, 2]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums2[0] 变为 6 。 nums1 = [1, 2, 3, 4, 5, 6], nums2 = [6, 1, 2, 2, 2, 2] 。
# - 将 nums1[5] 变为 1 。 nums1 = [1, 2, 3, 4, 5, 1], nums2 = [6, 1, 2, 2, 2, 2] 。
# - 将 nums1[2] 变为 2 。 nums1 = [1, 2, 2, 4, 5, 1], nums2 = [6, 1, 2, 2, 2, 2] 。

# 示例 2：
# 输入：nums1 = [1, 1, 1, 1, 1, 1, 1], nums2 = [6]
# 输出：- 1
# 解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。

# 示例 3：
# 输入：nums1 = [6, 6], nums2 = [1]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums1[0] 变为 2 。 nums1 = [2, 6], nums2 = [1] 。
# - 将 nums1[1] 变为 2 。 nums1 = [2, 2], nums2 = [1] 。
# - 将 nums2[0] 变为 4 。 nums1 = [2, 2], nums2 = [4] 。


# 提示：
# 1 <= nums1.length, nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 6

# 复习

from typing import List
# @lc code=start


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def getOpr(cnt1: List[int], cnt2: List[int], diff: int) -> int:
            '''
            cnt1 大，cnt2 小，diff 差值
            返回最少调整次数
            '''
            # 能让diff变到0以下（含0）即可
            res = 0
            for i in range(1, 6):
                avail = cnt1[7-i] + cnt2[i]  # 6-i 档 总共有这么多调的
                if diff > avail * (6-i):
                    diff -= avail * (6-i)
                    res += avail
                else:
                    res += (diff + (6-i) - 1) // (6-i)
                    break
            return res

        m, n = len(nums1), len(nums2)
        if 6 * m < n or m > 6 * n:
            # 这种情况下没有办法
            return -1

        diff = 0  # 记录两个数组合计之差
        cnt1 = [0] * 7
        for n in nums1:
            cnt1[n] += 1
            diff += n

        cnt2 = [0] * 7
        for n in nums2:
            cnt2[n] += 1
            diff -= n

        if diff == 0:
            return 0
        elif diff < 0:
            return getOpr(cnt2, cnt1, -diff)
        return getOpr(cnt1, cnt2, diff)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([5, 6, 4, 3, 1, 2], [
          6, 3, 3, 1, 4, 5, 3, 4, 1, 3, 4]))  # 4
    print(solution.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]))  # 3
    print(solution.minOperations([1, 1, 1, 1, 1, 1, 1], [6]))  # -1
    print(solution.minOperations([6, 6], [1]))  # 3

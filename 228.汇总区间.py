#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# 给定一个无重复元素的有序整数数组 nums 。
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，
# 并且不存在属于某个范围但不属于 nums 的数字 x 。

# 列表中的每个区间范围[a, b] 应该按如下格式输出：

# "a->b" ，如果 a != b
# "a" ，如果 a == b

# 示例 1：
# 输入：nums = [0, 1, 2, 4, 5, 7]
# 输出：["0->2", "4->5", "7"]
# 解释：区间范围是：
# [0, 2] - -> "0->2"
# [4, 5] - -> "4->5"
# [7, 7] - -> "7"

# 示例 2：
# 输入：nums = [0, 2, 3, 4, 6, 8, 9]
# 输出：["0", "2->4", "6", "8->9"]
# 解释：区间范围是：
# [0, 0] - -> "0"
# [2, 4] - -> "2->4"
# [6, 6] - -> "6"
# [8, 9] - -> "8->9"

# 示例 3：
# 输入：nums = []
# 输出：[]

# 示例 4：
# 输入：nums = [-1]
# 输出：["-1"]

# 示例 5：
# 输入：nums = [0]
# 输出：["0"]

# 提示：
# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# nums 中的所有值都 互不相同
# nums 按升序排列


from typing import List
# @lc code=start


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        pStart = None
        prev = None
        for num in nums:
            if pStart is None:
                pStart = num
            if prev is not None and prev != num - 1:
                # 新区间
                if pStart == prev:
                    res.append(str(pStart))
                else:
                    res.append("%d->%d" % (pStart, prev))
                pStart = num
            prev = num

        if prev == pStart:
            res.append(str(pStart))
        else:
            res.append("%d->%d" % (pStart, prev))

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(solution.summaryRanges([]))
    print(solution.summaryRanges([-1]))
    print(solution.summaryRanges([0]))

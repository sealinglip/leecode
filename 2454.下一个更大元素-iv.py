#
# @lc app=leetcode.cn id=2454 lang=python3
#
# [2454] 下一个更大元素 IV
#
# 给你一个下标从 0 开始的非负整数数组 nums 。对于 nums 中每一个整数，你必须找到对应元素的 第二大 整数。

# 如果 nums[j] 满足以下条件，那么我们称它为 nums[i] 的 第二大 整数：

# j > i
# nums[j] > nums[i]
# 恰好存在 一个 k 满足 i < k < j 且 nums[k] > nums[i] 。
# 如果不存在 nums[j] ，那么第二大整数为 -1 。

# 比方说，数组 [1, 2, 4, 3] 中，1 的第二大整数是 4 ，2 的第二大整数是 3 ，3 和 4 的第二大整数是 -1 。
# 请你返回一个整数数组 answer ，其中 answer[i]是 nums[i] 的第二大整数。

 
# 示例 1：
# 输入：nums = [2,4,0,9,6]
# 输出：[9,6,6,-1,-1]
# 解释：
# 下标为 0 处：2 的右边，4 是大于 2 的第一个整数，9 是第二个大于 2 的整数。
# 下标为 1 处：4 的右边，9 是大于 4 的第一个整数，6 是第二个大于 4 的整数。
# 下标为 2 处：0 的右边，9 是大于 0 的第一个整数，6 是第二个大于 0 的整数。
# 下标为 3 处：右边不存在大于 9 的整数，所以第二大整数为 -1 。
# 下标为 4 处：右边不存在大于 6 的整数，所以第二大整数为 -1 。
# 所以我们返回 [9,6,6,-1,-1] 。

# 示例 2：
# 输入：nums = [3,3]
# 输出：[-1,-1]
# 解释：
# 由于每个数右边都没有更大的数，所以我们返回 [-1,-1] 。
 

# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9

# Hard
# 复习

from typing import List
# @lc code=start
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        st2 = [] # 单调递减栈：保存已经出现了下一个更大元素的元素索引
        st1 = [] # 单调递减栈：保存未出现下一个更大元素的元素索引
        for i, x in enumerate(nums):
            while st2 and nums[st2[-1]] < x:
                res[st2.pop()] = x
            if st1 and nums[st1[-1]] < x:
                # 判断该插入到st1的哪个位置，把st1的剩余部分拼接到st2上去
                pos = len(st1) -1
                while pos >= 0 and nums[st1[pos]] < x:
                    pos -= 1
                st2 += st1[pos+1:]
                del st1[pos+1:]
            st1.append(i)

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.secondGreaterElement([2,4,0,9,6])) # [9,6,6,-1,-1]
    print(solution.secondGreaterElement([3,3])) # [-1,-1]
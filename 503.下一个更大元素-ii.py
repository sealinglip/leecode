#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 - 1。

# 示例 1:
# 输入: [1, 2, 1]
# 输出: [2, -1, 2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
# 注意: 输入数组的长度不会超过 10000。

from typing import List
# @lc code=start


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if not N:
            return []

        stack = []  # 单调栈，在栈里的都是未记录下一个更大数的位置索引
        res = [-1] * N
        for i in range(N << 1):  # 0 ~ N * 2
            num = nums[i % N]
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num
            if i < N:
                stack.append(i)
        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElements([1, 2, 1]))

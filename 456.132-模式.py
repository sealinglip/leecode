#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#
# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
# 注意：n 的值小于15000。

# 示例1:
# 输入: [1, 2, 3, 4]
# 输出: False
# 解释: 序列中不存在132模式的子序列。

# 示例 2:
# 输入: [3, 1, 4, 2]
# 输出: True
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

# 示例 3:
# 输入: [-1, 3, 2, 0]
# 输出: True
# 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和[-1, 2, 0].


from typing import List
# @lc code=start


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        # 解法1
        # stack = []
        # for num in nums:
        #     if not stack:
        #         stack.append(num)
        #     else:
        #         for i in range(len(stack) >> 1):
        #             if stack[i << 1] < num < stack[(i << 1) + 1]:
        #                 return True
        #         odd = len(stack) & 1  # 长度是否为奇数
        #         if odd:
        #             if num < stack[-1]:
        #                 stack[-1] = num
        #             elif num > stack[-1]:
        #                 stack.append(num)
        #         else:
        #             if num > stack[-1]:
        #                 stack[-1] = num
        #             elif num < stack[-2]:
        #                 stack.append(num)
        # return False
        # 效果：Your runtime beats 8.14 % of python3 submissions
        # Your memory usage beats 44.19 % of python3 submissions(15.6 MB)

        # 解法2
        stack = []
        numK = -2147483648  # Integer.MIN_MAX
        N = len(nums)
        for i in range(N - 1, -1, -1):
            num = nums[i]
            if num < numK:
                return True

            while stack and num > stack[-1]:
                numK = stack.pop()

            stack.append(num)

        return False
        # Your runtime beats 84.19 % of python3 submissions
        # Your memory usage beats 21.16 % of python3 submissions(15.6 MB)

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.find132pattern([1, 2, 3, 4]))
    print(solution.find132pattern([3, 1, 4, 2]))
    print(solution.find132pattern([-1, 3, 2, 0]))

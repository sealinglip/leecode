#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
# 进阶：你可以在 O(n) 的时间解决这个问题吗？

# 示例 1：
# 输入：nums = [3, 10, 5, 25, 2, 8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.

# 示例 2：
# 输入：nums = [0]
# 输出：0

# 示例 3：
# 输入：nums = [2, 4]
# 输出：6

# 示例 4：
# 输入：nums = [8, 10, 2]
# 输出：10

# 示例 5：
# 输入：nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
# 输出：127

# 提示：
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1

# 复习

from typing import List
# @lc code=start


class Trie:
    def __init__(self) -> None:
        self.left = None
        self.right = None

    def getOrCreateLeft(self) -> 'Trie':
        if self.left is None:
            self.left = Trie()
        return self.left

    def getOrCreateRight(self) -> 'Trie':
        if self.right is None:
            self.right = Trie()
        return self.right


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0
        elif N == 2:
            return nums[0] ^ nums[1]

        FLAG = 1 << 30

        root = Trie()
        # 初始化搜索树
        for n in nums:
            node = root
            # 从高位到低位构建搜索树
            f = FLAG
            while f:
                b = f & n  # 判断该位是否为1
                if b:
                    node = node.getOrCreateRight()
                else:
                    node = node.getOrCreateLeft()
                f >>= 1

        # 循环判断
        maxXor = 0
        for n in nums:
            node = root
            xor = 0
            f = FLAG
            while f:
                b = f & n  # 判断该位是否为1
                if b:
                    next = node.left
                else:
                    next = node.right
                if next:
                    xor |= f
                else:
                    next = node.left or node.right
                node = next
                f >>= 1
            if xor > maxXor:
                maxXor = xor

        return maxXor


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaximumXOR([3, 10, 5, 25, 2, 8])) # 28
    print(solution.findMaximumXOR([0])) # 0
    print(solution.findMaximumXOR([1])) # 0
    print(solution.findMaximumXOR([2, 4])) # 6
    print(solution.findMaximumXOR([8, 10, 2])) # 10
    print(solution.findMaximumXOR(
        [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])) # 127

#
# @lc app=leetcode.cn id=1707 lang=python3
#
# [1707] 与数组中元素的最大异或值
#
# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
# 第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，
# 其中所有 j 均满足 nums[j] <= mi 。
# 如果 nums 中的所有元素都大于 mi，最终答案就是 - 1 。
# 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。


# 示例 1：
# 输入：nums = [0, 1, 2, 3, 4], queries = [[3, 1], [1, 3], [5, 6]]
# 输出：[3, 3, 7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3=3 而 1 XOR 3=2 。二者中的更大值是 3 。
# 2) 1 XOR 2=3.
# 3) 5 XOR 2=7.

# 示例 2：
# 输入：nums=[5, 2, 4, 6, 6, 3], queries=[[12, 4], [8, 1], [6, 3]]
# 输出：[15, -1, 5]

# 提示：
# 1 <= nums.length, queries.length <= 10^5
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 10^9

from typing import List
# @lc code=start


class Trie:
    L = 30

    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.minVal = float('inf')

    def insert(self, val: int):
        node = self
        node.minVal = min(node.minVal, val)
        for i in range(Trie.L, -1, -1):
            b = (val >> i) & 1
            if b:
                if node.right is None:
                    node.right = Trie()
                node = node.right
            else:
                if node.left is None:
                    node.left = Trie()
                node = node.left
            node.minVal = min(node.minVal, val)

    def getMaxXor(self, val: int, limit: int) -> int:
        node = self
        if node.minVal > limit:
            return -1

        ans = 0
        for i in range(Trie.L, -1, -1):
            b = (val >> i) & 1
            hit = False
            if b:
                # 优选node.left的情况不需要判断node.left.minVal和limit的关系
                # 因为node.minVal <= limit，所以node.left如果不为空，则必定满足node.left.minVal <= limit
                # 如果node.left为空，则必定满足node.right.minVal <= limit
                if node.left:
                    node = node.left
                    hit = True
                else:
                    node = node.right
            else:
                if node.right and node.right.minVal <= limit:
                    node = node.right
                    hit = True
                else:
                    node = node.left
            if hit:
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 构建二叉搜索数
        t = Trie()
        for n in nums:
            t.insert(n)

        ans = []
        for x, m in queries:
            ans.append(t.getMaxXor(x, m))

        return ans

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))
    print(solution.maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]))

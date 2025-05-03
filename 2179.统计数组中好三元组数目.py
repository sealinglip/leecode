#
# @lc app=leetcode.cn id=2179 lang=python3
#
# [2179] 统计数组中好三元组数目
#
# https://leetcode.cn/problems/count-good-triplets-in-an-array/description/
#
# algorithms
# Hard (40.71%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 12.6K
# Testcase Example:  '[2,0,1,3]\n[0,1,2,3]'
#
# 给你两个下标从 0 开始且长度为 n 的整数数组 nums1 和 nums2 ，两者都是 [0, 1, ..., n - 1] 的 排列 。
# 
# 好三元组 指的是 3 个 互不相同 的值，且它们在数组 nums1 和 nums2 中出现顺序保持一致。换句话说，如果我们将 pos1v 记为值 v 在
# nums1 中出现的位置，pos2v 为值 v 在 nums2 中的位置，那么一个好三元组定义为 0 <= x, y, z <= n - 1 ，且
# pos1x < pos1y < pos1z 和 pos2x < pos2y < pos2z 都成立的 (x, y, z) 。
# 
# 请你返回好三元组的 总数目 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# 输出：1
# 解释：
# 总共有 4 个三元组 (x,y,z) 满足 pos1x < pos1y < pos1z ，分别是 (2,0,1) ，(2,0,3) ，(2,1,3) 和
# (0,1,3) 。
# 这些三元组中，只有 (0,1,3) 满足 pos2x < pos2y < pos2z 。所以只有 1 个好三元组。
# 
# 
# 示例 2：
# 
# 输入：nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
# 输出：4
# 解释：总共有 4 个好三元组 (4,0,3) ，(4,0,2) ，(4,1,3) 和 (4,1,2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length == nums2.length
# 3 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= n - 1
# nums1 和 nums2 是 [0, 1, ..., n - 1] 的排列。
# 
# 
# 复习

from typing import List

# @lc code=start
# 树状数组（Binary Indexed Tree）
class BinaryIndexedTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # pos2[i]记录的是数字i在nums2中的位置索引
        # pos22Pos1[i]记录nums2[i]在nums1中的位置索引
        pos2, pos22Pos1 = [0] * n, [0] * n
        for i, num in enumerate(nums2):
            pos2[num] = i
        for i, num in enumerate(nums1):
            pos22Pos1[pos2[num]] = i
        tree = BinaryIndexedTree(n)

        res = 0
        for i in range(n):
            # nums2[i] == nums1[pos]
            pos = pos22Pos1[i]
            # left是nums2[:i]的数，在nums1[:pos]中的个数
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (i - left)
            res += left * right

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.goodTriplets([2,0,1,3], [0,1,2,3])) # 1
    print(solution.goodTriplets([4,0,1,3,2], [4,1,0,2,3])) # 4

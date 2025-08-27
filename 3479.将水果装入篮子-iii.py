#
# @lc app=leetcode.cn id=3479 lang=python3
#
# [3479] 将水果装入篮子 III
#
# https://leetcode.cn/problems/fruits-into-baskets-iii/description/
#
# algorithms
# Medium (37.40%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 23.1K
# Testcase Example:  '[4,2,5]\n[3,5,4]'
#
# 给你两个长度为 n 的整数数组，fruits 和 baskets，其中 fruits[i] 表示第 i 种水果的 数量，baskets[j] 表示第 j
# 个篮子的 容量。
# 
# 你需要对 fruits 数组从左到右按照以下规则放置水果：
# 
# 每种水果必须放入第一个 容量大于等于 该水果数量的 最左侧可用篮子 中。
# 每个篮子只能装 一种 水果。
# 如果一种水果 无法放入 任何篮子，它将保持 未放置。
# 
# 返回所有可能分配完成后，剩余未放置的水果种类的数量。
# 
# 
# 示例 1
# 输入： fruits = [4,2,5], baskets = [3,5,4]
# 输出： 1
# 解释：
# fruits[0] = 4 放入 baskets[1] = 5。
# fruits[1] = 2 放入 baskets[0] = 3。
# fruits[2] = 5 无法放入 baskets[2] = 4。
# 
# 由于有一种水果未放置，我们返回 1。
# 
# 示例 2
# 输入： fruits = [3,6,1], baskets = [6,4,7]
# 输出： 0
# 解释：
# fruits[0] = 3 放入 baskets[0] = 6。
# fruits[1] = 6 无法放入 baskets[1] = 4（容量不足），但可以放入下一个可用的篮子 baskets[2] = 7。
# fruits[2] = 1 放入 baskets[1] = 4。
# 由于所有水果都已成功放置，我们返回 0。
# 
# 
# 提示：
# n == fruits.length == baskets.length
# 1 <= n <= 10^5
# 1 <= fruits[i], baskets[i] <= 10^9
# 
# 
#

# 线段树
from typing import List
# @lc code=start

class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.ma = [0] * (2 << (n-1).bit_length())# 记录区域子树的最大值
        self.baskets = nums
        self.buildTree(nums, 1, 0, n-1)
    
    def buildTree(self, nums: List[int], o: int, l: int, r: int) -> None:
        if l == r:
            self.ma[o] = nums[l]
            return
        mid = (l + r) >> 1
        self.buildTree(nums, o << 1, l, mid)
        self.buildTree(nums, (o << 1) + 1, mid + 1, r)
        self.ma[o] = max(self.ma[o << 1], self.ma[(o << 1) + 1])

    def findAndUpdate(self, o: int, l: int, r: int, x: int) -> int:
        if self.ma[o] < x:
            return -1
        if l == r:
            self.ma[o] = -1
            return l
        mid = (l + r) >> 1
        i = self.findAndUpdate(o << 1, l, mid, x)
        if i < 0:
            i = self.findAndUpdate((o << 1) + 1, mid + 1, r, x)
        self.ma[o] = max(self.ma[o << 1], self.ma[(o << 1) + 1])
        return i

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t = SegmentTree(baskets)
        n = len(baskets)
        res = 0
        for x in fruits:
            if t.findAndUpdate(1, 0, n-1, x) < 0:
                res += 1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numOfUnplacedFruits([4,2,5], [3,5,4])) # 1
    print(solution.numOfUnplacedFruits([3,6,1], [6,4,7])) # 0

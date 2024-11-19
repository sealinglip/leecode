#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# 给你一个数组 nums ，请你完成两类查询。

# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
# 实现 NumArray 类：

# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）


# 示例 1：
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
# 解释：
# NumArray numArray = new NumArray([1, 3, 5])
# numArray.sumRange(0, 2)
# // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2)
# // nums = [1, 2, 5]
# numArray.sumRange(0, 2)
# // 返回 1 + 2 + 5 = 8


# 提示：
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 10^4

# 复习
from typing import List
# @lc code=start

# 方法1 - 分区
# SEC_SIZE = 50  # 分区大小
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.secSum = [0] * ((len(nums) + SEC_SIZE - 1) // SEC_SIZE)  # 分区求和
#         for i, num in enumerate(nums):
#             j = i // SEC_SIZE
#             self.secSum[j] += num

#     def update(self, index: int, val: int) -> None:
#         delta = val - self.nums[index]
#         self.nums[index] = val
#         self.secSum[index // SEC_SIZE] += delta

#     def sumRange(self, left: int, right: int) -> int:
#         i = left // SEC_SIZE
#         j = right // SEC_SIZE
#         # 和由三部分组成
#         if i == j:
#             return sum(self.nums[left:right+1], 0)
#         else:
#             return sum(self.nums[left:(i+1)*SEC_SIZE]) + sum(self.secSum[i+1:j]) + sum(self.nums[j*SEC_SIZE:right+1])

# 方法2 - 树状数组（Binary Indexed Tree）
# class NumArray:
#     __slots__ = 'n', 'nums', 'tree'

#     def __init__(self, nums: List[int]):
#         n = len(nums)
#         tree = [0] * (n+1)
#         for i, x in enumerate(nums, 1):
#             tree[i] += x
#             up = i + (i & -i)
#             if up <= n:
#                 tree[up] += x
#         self.n = n
#         self.nums = nums
#         self.tree = tree

#     def update(self, index: int, val: int) -> None:
#         delta = val - self.nums[index]
#         self.nums[index] = val
#         index += 1 # self.tree以1为基
#         while index <= self.n:
#             self.tree[index] += delta
#             index += index & (-index)

#     def prefixSum(self, i: int) -> int:
#         s = 0
#         while i:
#             s += self.tree[i]
#             i -= i & -i
#         return s

#     def sumRange(self, left: int, right: int) -> int:
#         return self.prefixSum(right+1) - self.prefixSum(left)
    

# 方法3 —— 线段树（Segment Tree）

class NumArray:
    __slots__ = 'n', 'tree'

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n << 1)
        self.build(nums)

    def build(self, data: List[int]) -> None:
        # 将数据填充到叶子节点
        self.tree[-self.n:] = data
        # 构建树
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 1:
            index >>= 1
            self.tree[index] = self.tree[index << 1] + self.tree[index << 1 | 1]

    def sumRange(self, left: int, right: int) -> int:
        # 查询区间[left, right]
        res = 0
        # 转成开区间
        left += self.n - 1
        right += self.n + 1
        while (left ^ right) != 1:
            if left & 1 == 0:
                res += self.tree[left^1] # left+1
            if right & 1 == 1:
                res += self.tree[right^1] # right-1

            left >>= 1
            right >>= 1
        return res

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(index,val)
        # param_2 = obj.sumRange(left,right)
        # @lc code=end
if __name__ == "__main__":
    numArray = NumArray([1, 3, 5])
    print(numArray.sumRange(0, 2)) # 9
    numArray.update(1, 2)
    print(numArray.sumRange(0, 2)) # 8
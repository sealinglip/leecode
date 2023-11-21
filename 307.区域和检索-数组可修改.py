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
SEC_SIZE = 50  # 分区大小


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.secSum = [0] * ((len(nums) + SEC_SIZE - 1) // SEC_SIZE)  # 分区求和
        for i, num in enumerate(nums):
            j = i // SEC_SIZE
            self.secSum[j] += num

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.secSum[index // SEC_SIZE] += delta

    def sumRange(self, left: int, right: int) -> int:
        i = left // SEC_SIZE
        j = right // SEC_SIZE
        # 和由三部分组成
        if i == j:
            return sum(self.nums[left:right+1], 0)
        else:
            return sum(self.nums[left:(i+1)*SEC_SIZE]) + sum(self.secSum[i+1:j]) + sum(self.nums[j*SEC_SIZE:right+1])

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
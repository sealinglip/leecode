#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest 类：
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

# 示例：
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2])
# kthLargest.add(3) // return 4
# kthLargest.add(5) // return 5
# kthLargest.add(10) // return 5
# kthLargest.add(9) // return 8
# kthLargest.add(4) // return 8

# 提示：
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# 最多调用 add 方法 10^4 次
# 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素

from typing import List
# @lc code=start
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = nums[:min(k, len(nums))]
        self.k = k
        heapq.heapify(self.hq)
        if len(nums) > k:
            for num in nums[k:]:
                heapq.heappushpop(self.hq, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)
        return self.hq[0]

        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
        # @lc code=end
if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))

# 给你一个二进制数组 nums。
# 你可以对数组执行以下操作 任意 次（也可以 0 次）：
# 选择数组中 任意 一个下标 i ，并将从下标 i 开始一直到数组末尾 所有 元素 反转 。
# 反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
# 请你返回将 nums 中所有元素变为 1 的 最少 操作次数。

# 示例 1：
# 输入：nums = [0,1,1,0,1]
# 输出：4
# 解释：
# 我们可以执行以下操作：
# 选择下标 i = 1 执行操作，得到 nums = [0,0,0,1,0] 。
# 选择下标 i = 0 执行操作，得到 nums = [1,1,1,0,1] 。
# 选择下标 i = 4 执行操作，得到 nums = [1,1,1,0,0] 。
# 选择下标 i = 3 执行操作，得到 nums = [1,1,1,1,1] 。

# 示例 2：
# 输入：nums = [1,0,0,0]
# 输出：1
# 解释：
# 我们可以执行以下操作：
# 选择下标 i = 1 执行操作，得到 nums = [1,1,1,1] 。
 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 1

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 从后往前数，到最早的一个为零段，有多少个切换，就得有多少次操作
        # 实际操作时，从前往后数也是一样的，判断第0个元素是否为0，如果为1，总段数减1
        res = 0 # 记录切换次数，段数 = 切换次数 + 1
        n = len(nums)
        prev = nums[0]
        for i in range(1, n):
            if nums[i] != prev:
                res += 1
                prev = nums[i]

        return res + 1 if nums[0] == 0 else res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([0,1,1,0,1])) # 4
    print(solution.minOperations([1,0,0,0])) # 1

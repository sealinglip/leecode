#
# @lc app=leetcode.cn id=1671 lang=python3
#
# [1671] 得到山形数组的最少删除次数
#
# 我们定义 arr 是 山形数组 当且仅当它满足：

# arr.length >= 3
# 存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。


# 示例 1：
# 输入：nums = [1,3,1]
# 输出：0
# 解释：数组本身就是山形数组，所以我们不需要删除任何元素。

# 示例 2：
# 输入：nums = [2,1,1,5,6,2,3,1]
# 输出：3
# 解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
 

# 提示：
# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 10^9
# 题目保证 nums 删除一些元素后一定能得到山形数组。

# 复习

from typing import List
from bisect import bisect_left
# @lc code=start
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # 以每个位置为顶峰分别求左侧最长递增子序列和右侧最长递减子序列长度，相加求最大值即为答案
        l = self.getLIS(nums)
        r = self.getLIS(nums[::-1])[::-1]
        
        return len(nums) - max(li + ri for li, ri in zip(l, r) if li > 1 and ri > 1) + 1
    
    def getLIS(self, nums: List[int]) -> List[int]:
        l = [] # 记 l[i] 为以i为顶峰，左侧最长递增子序列的长度（含自己）
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
                l.append(len(d))
            else:
                i = bisect_left(d, n)
                d[i] = n
                l.append(i+1)
        return l


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumMountainRemovals([9,8,1,7,6,5,4,3,2,1])) # 2
    print(solution.minimumMountainRemovals([4,3,2,1,1,2,3,1])) # 4
    print(solution.minimumMountainRemovals([1,3,1])) # 0
    print(solution.minimumMountainRemovals([2,1,1,5,6,2,3,1])) # 3

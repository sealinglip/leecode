#
# @lc app=leetcode.cn id=2576 lang=python3
#
# [2576] 求出最多标记下标
#
# 给你一个下标从 0 开始的整数数组 nums 。

# 一开始，所有下标都没有被标记。你可以执行以下操作任意次：

# 选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
# 请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。

# 示例 1：
# 输入：nums = [3,5,2,4]
# 输出：2
# 解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
# 没有其他更多可执行的操作，所以答案为 2 。

# 示例 2：
# 输入：nums = [9,2,5,4]
# 输出：4
# 解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
# 第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
# 没有其他更多可执行的操作，所以答案为 4 。

# 示例 3：
# 输入：nums = [7,6,8]
# 输出：0
# 解释：没有任何可以执行的操作，所以答案为 0 。

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9

from typing import List
# @lc code=start
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # 折半查找pivot点，nums[:pivot]都能在nums【pivot:]中找到大于等于自己两倍的值
        def bestSplit(pivot: int) -> int:
            '''
            最佳划分，返回0
            偏左，返回1
            偏右，返回-1
            '''
            l = 0
            r = pivot
            for l in range(pivot):
                v = nums[l] << 1
                while r < n and nums[r] < v:
                    r += 1
                if r == n:
                    # 右边的数不够用
                    return -1
                r += 1
            if (nums[pivot] << 1) <= nums[-1]:
                if (r < n - 1) or (r < n and bestSplit(pivot+1) == 0): # 右侧还剩俩或
                    # 切分点偏左
                    return 1
            return 0
                
        l = 0
        r = n >> 1
        while l <= r:
            m = (l + r) >> 1
            s = bestSplit(m)
            if s == 1:
                l = m + 1
            elif s == -1:
                r = m - 1
            else:
                return m << 1 # m代表对数，要返回个数，还要乘2

        return 0
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxNumOfMarkedIndices([4,16,58,52,51,53,67,29,12,42,67,76,95,51,31,49,9,72,83,84,12,85,78,73,3,48,22,59,99,63,10,21,43,77,43,74,75,27,13,29,73,13,20,6,56,75,83,26,24,53,56,61,96,57,33,89,99,93,81,28,49,80,88,29,51,26,95,35,61,31,96,15,65,87,12,15,81,38,96,58,23,85,5,81,26])) # 76
    print(solution.maxNumOfMarkedIndices([57,40,57,51,90,51,68,100,24,39,11,85,2,22,67,29,74,82,10,96,14,35,25,76,26,54,29,44,63,49,73,50,95,89,43,62,24,88,88,36,6,16,14,2,42,42,60,25,4,58,23,22,27,26,3,79,64,20,92])) # 58
    print(solution.maxNumOfMarkedIndices([3,5,2,4])) # 2
    print(solution.maxNumOfMarkedIndices([9,2,5,4])) # 4
    print(solution.maxNumOfMarkedIndices([7,6,8])) # 0

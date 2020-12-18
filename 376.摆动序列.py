#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。
# 少于两个元素的序列也是摆动序列。

# 例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 
# 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

# 给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

# 示例 1:
# 输入: [1,7,4,9,2,5]
# 输出: 6 
# 解释: 整个序列均为摆动序列。

# 示例 2:
# 输入: [1,17,5,10,13,15,10,5,16,8]
# 输出: 7
# 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

# 示例 3:
# 输入: [1,2,3,4,5,6,7,8,9]
# 输出: 2

# 进阶:
# 你能否用 O(n) 时间复杂度完成此题?

from typing import List
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        N = len(nums)
        if N < 2:
            return N

        # 方法1：动态规划
        # # 记up为截至当前位置，可以抽取的最后一个摆动为升序的摆动子序列长度，down为截至当前位置，可以抽取的最后一个摆动为降序的摆动子序列长度
        # up = down = 1 # 起始为1
        # for i in range(1, N):
        #     if nums[i] > nums[i - 1]:
        #         up = down + 1
        #     elif nums[i] < nums[i - 1]:
        #         down = up + 1
        
        # return max(up, down)

        # 方法2：贪心算法
        # 实际上就是求峰和谷的数量
        # 因为返回的合乎条件的最大长度的摆动子序列，即使其中某个元素不是峰或谷，也可以被替换为实际的峰和谷而不影响子序列的长度
        # 所以可以通过就用峰和谷来构造合乎条件的子序列
        preDiff = nums[1] - nums[0]
        res = 1 if preDiff == 0 else 2
        for i in range(2, N):
            diff = nums[i] - nums[i - 1]
            # 注意下面的preDiff判断条件要包含等于0的情况
            if (diff > 0 and preDiff <= 0) or (diff < 0 and preDiff >= 0):
                res += 1
                preDiff = diff

        return res


        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.wiggleMaxLength([3,3,3,2,5]))
    print(solution.wiggleMaxLength([1,1]))
    print(solution.wiggleMaxLength([1,7,4,9,2,5]))
    print(solution.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(solution.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
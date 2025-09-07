#
# @lc app=leetcode.cn id=3495 lang=python3
#
# [3495] 使数组元素都变为零的最少操作次数
#
# https://leetcode.cn/problems/minimum-operations-to-make-array-elements-zero/description/
#
# algorithms
# Hard (44.36%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 12.5K
# Testcase Example:  '[[1,2],[2,4]]'
#
# 给你一个二维数组 queries，其中 queries[i] 形式为 [l, r]。每个 queries[i] 表示了一个元素范围从 l 到 r （包括
# l 和 r ）的整数数组 nums 。
# 
# 在一次操作中，你可以：
# 选择一个查询数组中的两个整数 a 和 b。
# 将它们替换为 floor(a / 4) 和 floor(b / 4)。
# 
# 你的任务是确定对于每个查询，将数组中的所有元素都变为零的 最少 操作次数。返回所有查询结果的总和。
# 
# 
# 示例 1：
# 输入： queries = [[1,2],[2,4]]
# 输出： 3
# 解释：
# 对于 queries[0]：
# 初始数组为 nums = [1, 2]。
# 在第一次操作中，选择 nums[0] 和 nums[1]。数组变为 [0, 0]。
# 所需的最小操作次数为 1。
# 对于 queries[1]：
# 初始数组为 nums = [2, 3, 4]。
# 在第一次操作中，选择 nums[0] 和 nums[2]。数组变为 [0, 3, 1]。
# 在第二次操作中，选择 nums[1] 和 nums[2]。数组变为 [0, 0, 0]。
# 所需的最小操作次数为 2。
# 输出为 1 + 2 = 3。
# 
# 示例 2：
# 输入： queries = [[2,6]]
# 输出： 4
# 解释：
# 对于 queries[0]：
# 初始数组为 nums = [2, 3, 4, 5, 6]。
# 在第一次操作中，选择 nums[0] 和 nums[3]。数组变为 [0, 3, 4, 1, 6]。
# 在第二次操作中，选择 nums[2] 和 nums[4]。数组变为 [0, 3, 1, 1, 1]。
# 在第三次操作中，选择 nums[1] 和 nums[2]。数组变为 [0, 0, 0, 1, 1]。
# 在第四次操作中，选择 nums[3] 和 nums[4]。数组变为 [0, 0, 0, 0, 0]。
# 所需的最小操作次数为 4。
# 输出为 4。
# 
# 
# 提示：
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# queries[i] == [l, r]
# 1 <= l < r <= 10^9
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # 一个数x要转换多少次才能变成0
        # n = (x.bit_length() + 1) >> 1
        # 构建速查表
        # cheatsheet[i] 表示[1, 2^(i+1))之间的所有数通过转换操作floor(x / 4)要变成0需要的操作次数
        # 递推：[2^(i-1), 2^i)之间共有2^(i-1)个数，每个数二进制位长度均为i，那需要操作次数为 2^(i-1) * ((i+1)>>1)
        cheatsheet = [0] * 29 # 10^9 < 2^29
        cheatsheet[0] = 1
        for i in range(2, 30):
            cheatsheet[i-1] = cheatsheet[i-2] + (((i+1)>>1) << (i-1))

        def getAccumOps(x: int) -> int:
            if x <= 0:
                return 0
            elif x == 1:
                return cheatsheet[0]
            b = x.bit_length() - 1
            return cheatsheet[b-1] + (x + 1 - (1<<b)) * ((b+2) >> 1)

        res = 0
        for l, r in queries:
            # 先求[1, r]需要的操作次数，然后减掉[1,l-1]需要的操作次数
            ops = getAccumOps(r) - getAccumOps(l-1)
            # 根据题意，一次能操作两个数，所以实际需要的操作数可减半
            res += (ops+1) >> 1
        
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([[1,2],[2,4]])) # 3
    print(solution.minOperations([[2,6]])) # 4

#
# @lc app=leetcode.cn id=3356 lang=python3
#
# [3356] 零数组变换 II
#
# https://leetcode.cn/problems/zero-array-transformation-ii/description/
#
# algorithms
# Medium (34.56%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 13.3K
# Testcase Example:  '[2,0,2]\n[[0,2,1],[0,2,1],[1,1,3]]'
#
# 给你一个长度为 n 的整数数组 nums 和一个二维数组 queries，其中 queries[i] = [li, ri, vali]。
# 每个 queries[i] 表示在 nums 上执行以下操作：
# 
# 将 nums 中 [li, ri] 范围内的每个下标对应元素的值 最多 减少 vali。
# 每个下标的减少的数值可以独立选择。
# 
# 零数组 是指所有元素都等于 0 的数组。
# 返回 k 可以取到的 最小非负 值，使得在 顺序 处理前 k 个查询后，nums 变成 零数组。如果不存在这样的 k，则返回 -1。
# 
# 
# 示例 1：
# 输入： nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
# 输出： 2
# 解释：
# 对于 i = 0（l = 0, r = 2, val = 1）：
# 在下标 [0, 1, 2] 处分别减少 [1, 0, 1]。
# 数组将变为 [1, 0, 1]。
# 
# 对于 i = 1（l = 0, r = 2, val = 1）：
# 在下标 [0, 1, 2] 处分别减少 [1, 0, 1]。
# 数组将变为 [0, 0, 0]，这是一个零数组。因此，k 的最小值为 2。
# 
# 示例 2：
# 输入： nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
# 输出： -1
# 解释：
# 对于 i = 0（l = 1, r = 3, val = 2）：
# 在下标 [1, 2, 3] 处分别减少 [2, 2, 1]。
# 数组将变为 [4, 1, 0, 0]。
# 
# 对于 i = 1（l = 0, r = 2, val = 1）：
# 在下标 [0, 1, 2] 处分别减少 [1, 1, 0]。
# 数组将变为 [3, 0, 0, 0]，这不是一个零数组。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 5 * 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5
#

from bisect import bisect_left
from typing import List
# @lc code=start
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        # 预处理nums，变成差分数组
        preSum = 0
        for i in range(n):
            nums[i] -= preSum
            preSum += nums[i]

        def judge(k: int) -> int:
            arr = list(nums)
            for i in range(k):
                l, r, v = queries[i]
                arr[l] -= v
                if r < n-1:
                    arr[r+1] += v
            # 从头遍历差分数组，如果有>0的元素，说明减不到0
            tmp = 0
            for v in arr:
                tmp += v
                if tmp > 0:
                    return 0
            return 1
        
        idx = bisect_left(range(m+1), 1, key=judge)
        return -1 if idx > m else idx
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minZeroArray([7,6,8], [[0,0,2],[0,1,5],[2,2,5],[0,2,4]])) # 4
    print(solution.minZeroArray([8,4], [[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]])) # 5
    print(solution.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]])) # 2
    print(solution.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]])) # -1

#
# @lc app=leetcode.cn id=2848 lang=python3
#
# [2848] 与车相交的点
#
# 给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。对于任意下标 i，nums[i] = [starti, endi] ，其中 starti 是第 i 辆车的起点，endi 是第 i 辆车的终点。

# 返回数轴上被车 任意部分 覆盖的整数点的数目。


# 示例 1：
# 输入：nums = [[3,6],[1,5],[4,7]]
# 输出：7
# 解释：从 1 到 7 的所有点都至少与一辆车相交，因此答案为 7 。

# 示例 2：
# 输入：nums = [[1,3],[5,8]]
# 输出：7
# 解释：1、2、3、5、6、7、8 共计 7 个点满足至少与一辆车相交，因此答案为 7 。
 

# 提示：
# 1 <= nums.length <= 100
# nums[i].length == 2
# 1 <= starti <= endi <= 100

from typing import List
# @lc code=start
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = 0
        prev = nums[0][0] - 1
        for s, e in nums:
            if prev >= e:
                continue
            if prev >= s:
                res += e - prev
            else:
                res += e - s + 1
            prev = e

        return res
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfPoints([[2,3],[3,9],[5,7],[4,10],[9,10]])) # 9
    print(solution.numberOfPoints([[4,4],[9,10],[9,10],[3,8]])) # 8
    print(solution.numberOfPoints([[3,6],[1,5],[4,7]])) # 7
    print(solution.numberOfPoints([[1,3],[5,8]])) # 7

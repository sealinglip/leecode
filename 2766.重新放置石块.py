#
# @lc app=leetcode.cn id=2766 lang=python3
#
# [2766] 重新放置石块
#
# 给你一个下标从 0 开始的整数数组 nums ，表示一些石块的初始位置。再给你两个长度 相等 下标从 0 开始的整数数组 moveFrom 和 moveTo 。

# 在 moveFrom.length 次操作内，你可以改变石块的位置。在第 i 次操作中，你将位置在 moveFrom[i] 的所有石块移到位置 moveTo[i] 。

# 完成这些操作后，请你按升序返回所有 有 石块的位置。

# 注意：

# 如果一个位置至少有一个石块，我们称这个位置 有 石块。
# 一个位置可能会有多个石块。
 

# 示例 1：
# 输入：nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]
# 输出：[5,6,8,9]
# 解释：一开始，石块在位置 1,6,7,8 。
# 第 i = 0 步操作中，我们将位置 1 处的石块移到位置 2 处，位置 2,6,7,8 有石块。
# 第 i = 1 步操作中，我们将位置 7 处的石块移到位置 9 处，位置 2,6,8,9 有石块。
# 第 i = 2 步操作中，我们将位置 2 处的石块移到位置 5 处，位置 5,6,8,9 有石块。
# 最后，至少有一个石块的位置为 [5,6,8,9] 。

# 示例 2：
# 输入：nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2]
# 输出：[2]
# 解释：一开始，石块在位置 [1,1,3,3] 。
# 第 i = 0 步操作中，我们将位置 1 处的石块移到位置 2 处，有石块的位置为 [2,2,3,3] 。
# 第 i = 1 步操作中，我们将位置 3 处的石块移到位置 2 处，有石块的位置为 [2,2,2,2] 。
# 由于 2 是唯一有石块的位置，我们返回 [2] 。
 

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= moveFrom.length <= 10^5
# moveFrom.length == moveTo.length
# 1 <= nums[i], moveFrom[i], moveTo[i] <= 10^9
# 测试数据保证在进行第 i 步操作时，moveFrom[i] 处至少有一个石块。

from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        cnt = Counter(nums)
        for f, t in zip(moveFrom, moveTo):
            c = cnt[f]
            cnt[f] -= c
            cnt[t] += c
        
        return sorted(k for k in cnt.keys() if cnt[k] > 0)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.relocateMarbles([1,6,7,8], [1,7,2], [2,9,5])) # [5,6,8,9]
    print(solution.relocateMarbles([1,1,3,3], [1,3], [2,2])) # [2]
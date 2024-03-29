#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#
# 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。

# 你可以进行如下操作至多 maxOperations 次：

# 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
# 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
# 你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。

# 请你返回进行上述操作后的最小开销。


# 示例 1：
# 输入：nums = [9], maxOperations = 2
# 输出：3
# 解释：
# - 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6, 3] 。
# - 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6, 3] -> [3, 3, 3] 。
# 装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。

# 示例 2：
# 输入：nums = [2, 4, 8, 2], maxOperations = 4
# 输出：2
# 解释：
# - 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2, 4, 8, 2] -> [2, 4, 4, 4, 2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2, 4, 4, 4, 2] -> [2, 2, 2, 4, 4, 2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2, 2, 2, 4, 4, 2] -> [2, 2, 2, 2, 2, 4, 2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2, 2, 2, 2, 2, 4, 2] -> [2, 2, 2, 2, 2, 2, 2, 2] 。
# 装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。

# 示例 3：
# 输入：nums = [7, 17], maxOperations = 2
# 输出：7


# 提示：
# 1 <= nums.length <= 10^5
# 1 <= maxOperations, nums[i] <= 10^9

# 复习

from typing import List
# @lc code=start


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 二分法
        left, right, res = 1, max(nums), 0
        while left <= right:
            mid = (left + right) >> 1
            ops = sum((n-1) // mid for n in nums)
            if ops <= maxOperations:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSize([567, 550, 752, 618, 949, 863, 255, 357, 92, 543, 60, 957, 663, 545, 36, 606, 965, 18, 630, 636, 258, 296, 623, 799, 210, 610, 557, 247, 698, 640, 424, 111, 697, 804, 622, 270, 326, 653, 634, 125, 260, 534, 671, 751, 910, 803, 920, 224, 737, 914, 362, 450, 140, 323, 543, 408, 784, 274, 460, 849, 451, 440, 508, 870, 979, 704, 78, 213, 691, 296, 528, 84, 853, 428, 316, 282, 443, 178, 942, 599, 314, 187, 981, 483, 281,
          533, 138, 547, 619, 424, 632, 872, 460, 56, 698, 267, 731, 604, 171, 798, 418, 803, 311, 89, 395, 467, 47, 324, 734, 617, 739, 205, 246, 237, 782, 568, 914, 856, 587, 987, 610, 182, 441, 809, 505, 319, 490, 797, 126, 167, 82, 326, 627, 608, 804, 594, 896, 968, 689, 351, 63, 890, 590, 960, 165, 747, 823, 836, 95, 682, 146, 181, 895, 843, 311, 80, 14, 674, 294, 212, 27, 664, 598, 172, 966, 145, 831, 512, 682, 653, 536, 275, 333, 35], 87))  # 536
    print(solution.minimumSize([9], 2))  # 3
    print(solution.minimumSize([2, 4, 8, 2], 4))  # 2
    print(solution.minimumSize([7, 17], 2))  # 7

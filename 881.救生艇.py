#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#
# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。


# 示例 1：
# 输入：people = [1, 2], limit = 3
# 输出：1
# 解释：1 艘船载(1, 2)

# 示例 2：
# 输入：people = [3, 2, 2, 1], limit = 3
# 输出：3
# 解释：3 艘船分别载(1, 2), (2) 和(3)

# 示例 3：
# 输入：people = [3, 5, 3, 4], limit = 5
# 输出：4
# 解释：4 艘船分别载(3), (3), (4), (5)

# 提示：
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000

from typing import List
# @lc code=start
from bisect import bisect


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)

        people.sort()  # 排序
        if people[0] > (limit >> 1):
            return N

        right = bisect(people, limit - people[0])
        res = N - right # right往右的都只能独占一条船，不能共享
        right -= 1
        left = 0
        while left <= right:
            if left == right:
                left += 1
                res += 1
            elif people[left] + people[right] <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                right -= 1
                res += 1

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numRescueBoats([1, 2], 3))  # 1
    print(solution.numRescueBoats([3, 2, 2, 1], 3))  # 3
    print(solution.numRescueBoats([3, 5, 3, 4], 5))  # 4

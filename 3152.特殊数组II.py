# 如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。
# 周洋哥有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [fromi, toi]，请你帮助周洋哥检查子数组 nums[fromi..toi] 是不是一个 特殊数组 。
# 返回布尔数组 answer，如果 nums[fromi..toi] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为 false 。

# 示例 1：
# 输入：nums = [3,4,1,2,6], queries = [[0,4]]
# 输出：[false]
# 解释：
# 子数组是 [3,4,1,2,6]。2 和 6 都是偶数。

# 示例 2：
# 输入：nums = [4,3,1,6], queries = [[0,2],[2,3]]
# 输出：[false,true]
# 解释：
# 子数组是 [4,3,1]。3 和 1 都是奇数。因此这个查询的答案是 false。
# 子数组是 [1,6]。只有一对：(1,6)，且包含了奇偶性不同的数字。因此这个查询的答案是 true。
 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

from itertools import pairwise
from typing import List
from bisect import bisect

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # 遍历一遍，把不符合规则的跳变点都找出来
        # fp = []
        # n = len(nums)
        # b = nums[0] & 1
        # for i in range(1, n):
        #     # 期望的奇偶性
        #     b = 1 - b
        #     if (nums[i] & 1) != b:
        #         fp.append(i)
        #         b = 1 - b

        # res = []
        # for s, e in queries:
        #     res.append(bisect(fp, s) == bisect(fp, e))
        
        # return res

        m = len(nums)
        s = [0]
        for x, y in pairwise(nums):
            s.append(s[-1] + (x % 2 == y % 2))
        return [s[t] == s[f] for f, t in queries]

if __name__ == "__main__":
    solution = Solution()
    print(solution.isArraySpecial([3,4,1,2,6], [[0,4]])) # [False]
    print(solution.isArraySpecial([3,4,1,2,6], [[0,4]])) # [False]
    print(solution.isArraySpecial([4,3,1,6], [[0,2],[2,3]])) # [False, True]

#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#
# 给你一个长度为 n 的整数数组 coins ，它代表你拥有的 n 个硬币。第 i 个硬币的值为 coins[i] 。如果你从这些硬币中选出一部分硬币，它们的和为 x ，那么称，你可以 构造 出 x 。

# 请返回从 0 开始（包括 0 ），你最多能 构造 出多少个连续整数。

# 你可能有多个相同值的硬币。


# 示例 1：
# 输入：coins = [1, 3]
# 输出：2
# 解释：你可以得到以下这些值：
# - 0：什么都不取[]
# - 1：取[1]
# 从 0 开始，你可以构造出 2 个连续整数。


# 示例 2：
# 输入：coins = [1, 1, 1, 4]
# 输出：8
# 解释：你可以得到以下这些值：
# - 0：什么都不取[]
# - 1：取[1]
# - 2：取[1, 1]
# - 3：取[1, 1, 1]
# - 4：取[4]
# - 5：取[4, 1]
# - 6：取[4, 1, 1]
# - 7：取[4, 1, 1, 1]
# 从 0 开始，你可以构造出 8 个连续整数。


# 示例 3：
# 输入：nums = [1, 4, 10, 3, 1]
# 输出：20


# 提示：
# coins.length == n
# 1 <= n <= 4 * 10^4
# 1 <= coins[i] <= 4 * 10^4

# 复习
# 贪心

from typing import List
# @lc code=start


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # 不妨设我们现在能构造出[0,x] 区间的整数，现在我们新增一个整数 y，那么我们可以构造出的区间为 [0,x] 和 [y,x+y]，
        # 那么如果 y≤x+1，则加入整数 y 后我们能构造出 [0,x+y] 区间的整数，否则我们还是只能构造出 [0,x] 区间的数字。
        # 因此我们每次从数组中找到未选择数字中的最小值来作为 y，因为如果此时的最小值 y 都不能更新区间 [0,x]，那么剩下的其他元素都不能更新区间 [0,x]。
        coins.sort()
        x = 1
        for y in coins:
            if y <= x:
                x += y
            else:
                break
        return x


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.getMaximumConsecutive([1, 3]))  # 2
    print(solution.getMaximumConsecutive([1, 1, 1, 4]))  # 8
    print(solution.getMaximumConsecutive([1, 4, 10, 3, 1]))  # 20

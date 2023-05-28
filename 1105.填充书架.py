#
# @lc app=leetcode.cn id=1105 lang=python3
#
# [1105] 填充书架
#
# 给定一个数组 books ，其中 books[i] = [thicknessi, heighti] 表示第 i 本书的厚度和高度。你也会得到一个整数 shelfWidth 。

# 按顺序 将这些书摆放到总宽度为 shelfWidth 的书架上。

# 先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelfWidth ），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。

# 需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。

# 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
# 每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。

# 以这种方式布置书架，返回书架整体可能的最小高度。


# 示例 1：
# 输入：books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth = 4
# 输出：6
# 解释：
# 3 层书架的高度和为 1 + 3 + 2 = 6 。
# 第 2 本书不必放在第一层书架上。

# 示例 2:
# 输入: books = [[1, 3], [2, 4], [3, 2]], shelfWidth = 6
# 输出: 4


# 提示：
# 1 <= books.length <= 1000
# 1 <= thicknessi <= shelfWidth <= 1000
# 1 <= heighti <= 1000


from bisect import bisect_left
from itertools import accumulate
from typing import List
# @lc code=start


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # 动态规划
        # 记dp(i)为前i本书的最小高度
        # dp(0) = 0
        n = len(books)
        dp = [0] * (n + 1)
        accumWidth = [0] + list(accumulate(b[0] for b in books))
        heights = list(b[1] for b in books)

        for i in range(n):
            # 计算本层以i结尾，最多能容纳几个
            j = bisect_left(accumWidth, max(
                accumWidth[i+1] - shelfWidth, 0)) - 1  # 累计宽度里加了个前置0，所以索引会比实际大1，这里减回去
            dp[i + 1] = min(dp[k+1] + max(heights[k+1:i+1])
                            for k in range(j, i))

        return dp[-1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minHeightShelves(
        [[7, 3], [8, 7], [2, 7], [2, 5]], 10))  # 15
    print(solution.minHeightShelves(
        [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))  # 6
    print(solution.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))  # 4

#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
# 给你一个整数 n ，按字典序返回范围[1, n] 内所有整数。

# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。


# 示例 1：
# 输入：n = 13
# 输出：[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

# 示例 2：
# 输入：n = 2
# 输出：[1, 2]


# 提示：

# 1 <= n <= 5 * 10^4

from typing import List
# @lc code=start


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [0] * n
        num = 1
        for i in range(n):
            res[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while (num + 1) > n or (num % 10) == 9:
                    num //= 10
                num += 1

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.lexicalOrder(10))  # [1,10,2,3,4,5,6,7,8,9]
    # [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    print(solution.lexicalOrder(13))
    print(solution.lexicalOrder(2))  # [1, 2]

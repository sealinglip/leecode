#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

# 示例 1:
# 输入: 2
# 输出: [0, 1, 1]

# 示例 2:
# 输入: 5
# 输出: [0, 1, 1, 2, 1, 2]

# 进阶:
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

from typing import List
# @lc code=start


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            # i & (i - 1)可以去掉i最右边的一个1（如果有），又 i & (i - 1）是比 i 小的，所以i & (i - 1)的1的个数已经在前面算过了，
            # 那么 i的1的个数就是 i & (i - 1)的1的个数加上1
            res.append(res[i & (i - 1)] + 1)
        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(2))
    print(solution.countBits(5))

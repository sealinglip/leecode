#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 - 1 。

# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 - 1 。


# 示例 1：
# 输入：n = 12
# 输出：21

# 示例 2：
# 输入：n = 21
# 输出：- 1


# 提示：
# 1 <= n <= 2^31 - 1

# @lc code=start
from bisect import bisect_right


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        LIMIT = 1 << 31
        s = str(n)
        # 从低位向高位遍历n的十进制数位，遇到高位比低位小的，替换这一高位
        arr = []
        prevC = None
        for i, c in enumerate(s[::-1]):
            if i > 0 and c < prevC:
                break
            prevC = c
            arr.append(c)
        else:
            return -1

        # n的十进制表达的最后(i+1)位数要重新排列
        pos = bisect_right(arr, c)
        hc = arr[pos]
        arr[pos] = c
        n = int(s[:len(s)-i-1] + hc + ("".join(arr)))
        if n >= LIMIT:
            return -1
        return n


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElement(2147483486))  # -1
    print(solution.nextGreaterElement(21))  # -1
    print(solution.nextGreaterElement(12))  # 21
    print(solution.nextGreaterElement(987635421))  # 987641235

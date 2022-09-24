#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#
# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

# 示例 1:
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。

# 示例 2:
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。

# 注意:
# 给定数字的范围是[0, 10^8]

# 复习

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        x = y = -1  # 记录要交换的位置，-1代表没啥可交换的
        maxIdx = n - 1  # 记录最大位的位置

        for i in range(n-1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                x, y = i, maxIdx

        if x == -1:
            return num
        s[x], s[y] = s[y], s[x]
        return int(''.join(s))


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSwap(2736))  # 7236
    print(solution.maximumSwap(9973))  # 9973

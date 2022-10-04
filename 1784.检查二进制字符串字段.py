#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#
# 给你一个二进制字符串 s ，该字符串 不含前导零 。

# 如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。

# 如果 s 中 由连续若干个 '1' 组成的字段 数量不超过 1，返回 true​​​ 。否则，返回 false 。


# 示例 1：
# 输入：s = "1001"
# 输出：false
# 解释：由连续若干个 '1' 组成的字段数量为 2，返回 false

# 示例 2：
# 输入：s = "110"
# 输出：true

# 提示：
# 1 <= s.length <= 100
# s[i]​​​​ 为 '0' 或 '1'
# s[0] 为 '1'

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        prevC = '0'
        for c in s:
            if prevC == '1' and c == '0':
                cnt += 1
            prevC = c
        if prevC == '1':
            cnt += 1
        return cnt <= 1


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkOnesSegment("1001"))  # False
    print(solution.checkOnesSegment("110"))  # True
    print(solution.checkOnesSegment("0110"))  # True
    print(solution.checkOnesSegment("011"))  # True

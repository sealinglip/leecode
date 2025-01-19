#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#
# Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。

# 为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。

# 比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
# 注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
# 但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。

# 比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
# 给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。

# 由于答案可能很大，将它对 109 + 7 取余 后返回。

# 示例 1：
# 输入：pressedKeys = "22233"
# 输出：8
# 解释：
# Alice 可能发出的文字信息包括：
# "aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
# 由于总共有 8 种可能的信息，所以我们返回 8 。

# 示例 2：
# 输入：pressedKeys = "222222222222222222222222222222222222"
# 输出：82876089
# 解释：
# 总共有 2082876103 种 Alice 可能发出的文字信息。
# 由于我们需要将答案对 10^9 + 7 取余，所以我们返回 2082876103 % (10^9 + 7) = 82876089 。
 

# 提示：
# 1 <= pressedKeys.length <= 10^5
# pressedKeys 只包含数字 '2' 到 '9' 。

# @lc code=start
from functools import cache


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7
        # 除7/9有4个字母之外，其他都是3个
        radix = {"7":4, "9":4}

        @cache
        def allPossible(r: int, count: int) -> int:
            if count < 0:
                return 0
            elif count == 0:
                return 1
            res = 0
            for i in range(min(r,count), 0, -1):
                res += allPossible(r, count-i)
            return res % MOD
        
        prev = pressedKeys[0]
        count = 0
        res = 1
        for c in pressedKeys + "0":
            if c == prev:
                count += 1
            else:
                res *= allPossible(radix.get(prev, 3), count)
                res %= MOD
                count = 1
                prev = c

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countTexts("444444444444444444444444444444448888888888888888999999999999333333333333333366666666666666662222222222222222666666666666666633333333333333338888888888888888222222222222222244444444444444448888888888888222222222222222288888888888889999999999999999333333333444444664")) # 537551452
    print(solution.countTexts("22233")) # 8
    print(solution.countTexts("222222222222222222222222222222222222")) # 82876089

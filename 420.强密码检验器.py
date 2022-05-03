#
# @lc app=leetcode.cn id=420 lang=python3
#
# [420] 强密码检验器
#
# 如果一个密码满足下述所有条件，则认为这个密码是强密码：
# 由至少 6 个，至多 20 个字符组成。
# 至少包含 一个小写 字母，一个大写 字母，和 一个数字 。
# 同一字符 不能 连续出现三次(比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 如果满足其他条件也可以算是强密码)。
# 给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0 。

# 在一步修改操作中，你可以：
# 插入一个字符到 password ，
# 从 password 中删除一个字符，或
# 用另一个字符来替换 password 中的某个字符。


# 示例 1：
# 输入：password = "a"
# 输出：5

# 示例 2：
# 输入：password = "aA1"
# 输出：3

# 示例 3：
# 输入：password = "1337C0d3"
# 输出：0


# 提示：
# 1 <= password.length <= 50
# password 由字母、数字、点 '.' 或者感叹号 '!'

# Hard

# @lc code=start

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        if n < 5:
            # 长度为5以下（不含）的密码，修改成强密码，其次数就是长度差值，通过插入字符，一定能同时满足密码长度、字符多样性和连续重复字符长度限制的条件
            return 6 - n
        else:
            lower = upper = digit = 0
            for c in password:
                if c.isupper():
                    upper = 1
                elif c.islower():
                    lower = 1
                elif c.isdigit():
                    digit = 1

            categories = lower + upper + digit
            if n < 6:
                return max(6 - n, 3 - categories)
            elif n < 21:
                replace = cnt = 0
                cur = ""

                for c in password:
                    if c == cur:
                        cnt += 1
                    else:
                        replace += cnt // 3
                        cnt = 1
                        cur = c

                replace += cnt // 3
                return max(replace, 3 - categories)
            else:
                # 替换次数和删除次数
                replace, remove = 0, n - 20
                # k mod 3 = 1 的组数，即删除 2 个字符可以减少 1 次替换操作
                rm2 = cnt = 0
                cur = "#"

                for ch in password:
                    if ch == cur:
                        cnt += 1
                    else:
                        if remove > 0 and cnt >= 3:
                            if cnt % 3 == 0:
                                # 如果是 k % 3 = 0 的组，那么优先删除 1 个字符，减少 1 次替换操作
                                remove -= 1
                                replace -= 1
                            elif cnt % 3 == 1:
                                # 如果是 k % 3 = 1 的组，那么存下来备用
                                rm2 += 1
                            # k % 3 = 2 的组无需显式考虑
                        replace += cnt // 3
                        cnt = 1
                        cur = ch

                if remove > 0 and cnt >= 3:
                    if cnt % 3 == 0:
                        remove -= 1
                        replace -= 1
                    elif cnt % 3 == 1:
                        rm2 += 1

                replace += cnt // 3

                # 使用 k % 3 = 1 的组的数量，由剩余的替换次数、组数和剩余的删除次数共同决定
                use2 = min(replace, rm2, remove // 2)
                replace -= use2
                remove -= use2 * 2
                # 由于每有一次替换次数就一定有 3 个连续相同的字符（k / 3 决定），因此这里可以直接计算出使用 k % 3 = 2 的组的数量
                use3 = min(replace, remove // 3)
                replace -= use3
                remove -= use3 * 3
                return (n - 20) + max(replace, 3 - categories)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.strongPasswordChecker("a"))  # 5
    print(solution.strongPasswordChecker("aA1"))  # 3
    print(solution.strongPasswordChecker("1337C0d3"))  # 0

#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#
# 给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

# 如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。


# 示例 1：
# 输入：s1 = "bank", s2 = "kanb"
# 输出：true
# 解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"

# 示例 2：
# 输入：s1 = "attack", s2 = "defend"
# 输出：false
# 解释：一次字符串交换无法使两个字符串相等

# 示例 3：
# 输入：s1 = "kelb", s2 = "kelb"
# 输出：true
# 解释：两个字符串已经相等，所以不需要进行字符串交换

# 示例 4：
# 输入：s1 = "abcd", s2 = "dcba"
# 输出：false


# 提示：
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 和 s2 仅由小写英文字母组成
# @lc code=start

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        c1 = d1 = c2 = d2 = None
        for s, d in zip(s1, s2):
            if s != d:
                if diff:
                    c2, d2 = s, d
                else:
                    c1, d1 = s, d
                diff += 1
                if diff > 2:
                    return False

        if diff == 1:
            return False
        return c1 == d2 and c2 == d1


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.areAlmostEqual("bank", "kanb"))  # True
    print(solution.areAlmostEqual("attack", "defend"))  # False
    print(solution.areAlmostEqual("kelb", "kelb"))  # True
    print(solution.areAlmostEqual("abcd", "dcba"))  # False

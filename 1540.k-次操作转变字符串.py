#
# @lc app=leetcode.cn id=1540 lang=python3
#
# [1540] K 次操作转变字符串
#
# 给你两个字符串 s 和 t ，你的目标是在 k 次操作以内把字符串 s 转变成 t 。

# 在第 i 次操作时（1 <= i <= k），你可以选择进行如下操作：

# 选择字符串 s 中满足 1 <= j <= s.length 且之前未被选过的任意下标 j （下标从 1 开始），并将此位置的字符切换 i 次。
# 不进行任何操作。
# 切换 1 个字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 'z' 切换后会变成 'a'）。第 i 次操作意味着该字符应切换 i 次

# 请记住任意一个下标 j 最多只能被操作 1 次。

# 如果在不超过 k 次操作内可以把字符串 s 转变成 t ，那么请你返回 true ，否则请你返回 false 。


# 示例 1：
# 输入：s = "input", t = "ouput", k = 9
# 输出：true
# 解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。

# 示例 2：
# 输入：s = "abc", t = "bcd", k = 10
# 输出：false
# 解释：我们需要将每个字符切换 1 次才能得到 t 。我们可以在第 1 次操作时将 'a' 切换成 'b' ，但另外 2 个字母在剩余操作中无法再转变为 t 中对应字母。

# 示例 3：
# 输入：s = "aab", t = "bbb", k = 27
# 输出：true
# 解释：第 1 次操作时，我们将第一个 'a' 切换 1 次得到 'b' 。在第 27 次操作时，我们将第二个字母 'a' 切换 27 次得到 'b' 。
 

# 提示：
# 1 <= s.length, t.length <= 10^5
# 0 <= k <= 10^9
# s 和 t 只包含小写英文字母。

# @lc code=start
from collections import Counter


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        def op(c1: str, c2: str) -> int:
            res = ord(c2) - ord(c1)
            if res < 0:
                res += 26
            return res

        # 下面的解法会TLE
        # ops = [op(c1, c2) for c1, c2 in zip(s, t) if c1 != c2]
        # used = set()
        # for o in ops:
        #     while o in used:
        #         o += 26
        #     if o <= k:
        #         used.add(o)
        #     else:
        #         return False
        
        # return True

        # 改进，去重计数
        ops = Counter(op(c1, c2) for c1, c2 in zip(s, t) if c1 != c2)
        return len(ops) == 0 or max((v-1) * 26 + k for k, v in ops.items()) <= k

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.canConvertString("leetcode", "leetcode", 0)) # True
    print(solution.canConvertString("input", "ouput", 9)) # True
    print(solution.canConvertString("abc", "bcd", 10)) # False
    print(solution.canConvertString("aab", "bbb", 27)) # True

#
# @lc app=leetcode.cn id=1220 lang=python3
#
# [1220] 统计元音字母序列的数目
#
# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，所以请你返回 模 10 ^ 9 + 7 之后的结果。


# 示例 1：
# 输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i", "o" 和 "u"。

# 示例 2：
# 输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。

# 示例 3：
# 输入：n = 5
# 输出：68


# 提示：
# 1 <= n <= 2 * 10 ^ 4


# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 动规，不知道会不会超时，先试试
        cache = {}  # 缓存结果，key为（首字母, 长度），value为可能的字符串个数

        def dfs(initial: str, n: int) -> int:
            key = (initial, n)
            if n == 1:
                return 1
            res = cache.get(key)
            if not res:
                n -= 1
                if initial == 'a':
                    res = dfs('e', n)
                elif initial == 'e':
                    res = dfs('a', n) + dfs('i', n)
                elif initial == 'i':
                    res = dfs('a', n) + dfs('o', n) + dfs('e', n) + dfs('u', n)
                elif initial == 'o':
                    res = dfs('i', n) + dfs('u', n)
                elif initial == 'u':
                    res = dfs('a', n)

                res = res % MOD
                cache[key] = res
            return res

        return (dfs('a', n) + dfs('e', n) + dfs('i', n) + dfs('o', n) + dfs('u', n)) % MOD


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countVowelPermutation(1))  # 5
    print(solution.countVowelPermutation(2))  # 10
    print(solution.countVowelPermutation(5))  # 68
    print(solution.countVowelPermutation(144))  # 18208803

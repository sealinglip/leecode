# 给你两个字符串 word1 和 word2 。
# 如果一个字符串 x 重新排列后，word2 是重排字符串的 
# 前缀，那么我们称字符串 x 是 合法的 。

# 请你返回 word1 中 合法 子字符串的数目。


# 示例 1：
# 输入：word1 = "bcca", word2 = "abc"
# 输出：1
# 解释：
# 唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。

# 示例 2：
# 输入：word1 = "abcabc", word2 = "abc"
# 输出：10
# 解释：
# 除了长度为 1 和 2 的所有子字符串都是合法的。

# 示例 3：
# 输入：word1 = "abcabc", word2 = "aaabc"
# 输出：0


# 解释：
# 1 <= word1.length <= 10^5
# 1 <= word2.length <= 10^4
# word1 和 word2 都只包含小写英文字母。


from collections import Counter, defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        requirement = Counter(word2)
        res = 0
        n = len(word1)
        accum = defaultdict(int)

        def meetRequirement() -> bool:
            return all(accum[i] >= requirement[i] for i in requirement)
        
        l = r = 0
        while r < n:
            while r < n and not meetRequirement():
                accum[word1[r]] += 1
                r += 1
            while l < r and meetRequirement():
                res += n - r + 1
                accum[word1[l]] -= 1
                l += 1

        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.validSubstringCount("bcca", "abc")) # 1
    print(solution.validSubstringCount("abcabc", "abc")) # 10
    print(solution.validSubstringCount("abcabc", "aaabc")) # 0
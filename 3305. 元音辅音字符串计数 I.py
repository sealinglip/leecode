# 给你一个字符串 word 和一个 非负 整数 k。
# 返回 word 的 子字符串 中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，并且 恰好 包含 k 个辅音字母的子字符串的总数。


# 示例 1：
# 输入：word = "aeioqq", k = 1
# 输出：0
# 解释：
# 不存在包含所有元音字母的子字符串。

# 示例 2：
# 输入：word = "aeiou", k = 0
# 输出：1
# 解释：
# 唯一一个包含所有元音字母且不含辅音字母的子字符串是 word[0..4]，即 "aeiou"。

# 示例 3：
# 输入：word = "ieaouqqieaouqq", k = 1
# 输出：3
# 解释：
# 包含所有元音字母并且恰好含有一个辅音字母的子字符串有：
# word[0..5]，即 "ieaouq"。
# word[6..11]，即 "qieaou"。
# word[7..12]，即 "ieaouq"。
 

# 提示：
# 5 <= word.length <= 250
# word 仅由小写英文字母组成。
# 0 <= k <= word.length - 5

# 复习

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def count(m: int) -> int:
            """
            统计五个元音至少一次，辅音至少m次的子字符串个数
            """
            # 双指针
            r = consonants = res = 0
            vowelCnt = {}
            lb = n - 4 - m
            for l in range(lb):
                # 当前不满足条件
                # 如果是元音不够或者辅音不够，向右拓展右指针
                while r < n and (len(vowelCnt) < 5 or consonants < m):
                    if word[r] in vowels:
                        vowelCnt[word[r]] = vowelCnt.get(word[r], 0) + 1
                    else:
                        consonants += 1
                    r += 1
                # 如果满足条件
                if consonants >= m and len(vowelCnt) == 5:
                    # word[l:r] 满足条件
                    res += n - r + 1
                    
                if word[l] in vowels:
                    vowelCnt[word[l]] -= 1
                    if vowelCnt[word[l]] == 0:
                        del vowelCnt[word[l]]
                else:
                    consonants -= 1
            
            return res
                
        return count(k) - count(k + 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.countOfSubstrings("ieiaoud", 0)) # 2
    print(solution.countOfSubstrings("iqeaouqi", 2)) # 3
    print(solution.countOfSubstrings("aeioqq", 1)) # 0
    print(solution.countOfSubstrings("aeiou", 0)) # 1
    print(solution.countOfSubstrings("ieaouqqieaouqq", 1)) # 3

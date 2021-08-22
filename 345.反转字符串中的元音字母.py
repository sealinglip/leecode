#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c: str) -> bool:
            return c == 'a' or c == 'o' or c == 'e' or c == 'i' or c == 'u' or c == 'A' or c == 'O' or c == 'E' or c == 'I' or c == 'U'

        N = len(s)
        cArr = [c for c in s]
        vowelIndices = [i for i in range(N) if isVowel(s[i])]
        M = len(vowelIndices)
        for i in range(M >> 1):
            cArr[vowelIndices[i]], cArr[vowelIndices[M-1-i]
                                        ] = cArr[vowelIndices[M-1-i]], cArr[vowelIndices[i]]

        return "".join(cArr)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("aA"))  # Aa
    print(solution.reverseVowels("hello"))  # holle
    print(solution.reverseVowels("leetcode"))  # leotcede

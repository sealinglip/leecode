#
# @lc app=leetcode.cn id=2663 lang=python3
#
# [2663] 字典序最小的美丽字符串
#
# 如果一个字符串满足以下条件，则称其为 美丽字符串 ：

# 它由英语小写字母表的前 k 个字母组成。
# 它不包含任何长度为 2 或更长的回文子字符串。
# 给你一个长度为 n 的美丽字符串 s 和一个正整数 k 。

# 请你找出并返回一个长度为 n 的美丽字符串，该字符串还满足：在字典序大于 s 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。

# 对于长度相同的两个字符串 a 和 b ，如果字符串 a 在与字符串 b 不同的第一个位置上的字符字典序更大，则字符串 a 的字典序大于字符串 b 。

# 例如，"abcd" 的字典序比 "abcc" 更大，因为在不同的第一个位置（第四个字符）上 d 的字典序大于 c 。
 

# 示例 1：
# 输入：s = "abcz", k = 26
# 输出："abda"
# 解释：字符串 "abda" 既是美丽字符串，又满足字典序大于 "abcz" 。
# 可以证明不存在字符串同时满足字典序大于 "abcz"、美丽字符串、字典序小于 "abda" 这三个条件。

# 示例 2：
# 输入：s = "dc", k = 4
# 输出：""
# 解释：可以证明，不存在既是美丽字符串，又字典序大于 "dc" 的字符串。
 

# 提示：
# 1 <= n == s.length <= 10^5
# 4 <= k <= 26
# s 是一个美丽字符串

# Hard

# @lc code=start
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        # 从后往前依次试下能不能修改，改后能不能搞出一个美丽字符串出来
        # 要想不出现回文子串，那么任何一个位置的字符不能和前两个位置的字符相同
        def genBeautifulStr(i: int, j: int) -> str:
            """
            i位置的字符，上翻j，后续位置依次调整（在a~c中轮流排即可），返回新的美丽字符串
            """
            chArr = list(s)
            chArr[i] = chr(ord(s[i]) + j)
            # 先根据chArr[i-1](如果有的话)和chArr[i]确定后面的pattern
            pattern = ['a'] * 5
            pattern[1] = chArr[i]
            pattern[0] = chArr[max(0, i-1)]
            for j in range(2, 5):
                forbidden = pattern[j-2:j]
                for k in range(3):
                    c = chr(ord('a') + k)
                    if c not in forbidden:
                        pattern[j] = c
                        break
            pattern = pattern[2:] # 去掉前面两个辅助

            k = 0
            for j in range(i+1, len(s)):
                chArr[j] = pattern[k]
                k += 1
                if k == 3:
                    k = 0

            return "".join(chArr)

        for i in range(len(s)-1, -1, -1):
            # 位置i禁止字符
            forbidden = s[max(0,i-2):i]
            for j in range(1, 4):
                # 往上翻，还不能是禁止字符中的，禁止字符最多两个，最坏的情况是连翻两次都不行，第三次肯定可以（如果不行那就是到顶了），所以循环三次就可以了
                if ord(s[i]) - ord('a') + j < k and chr(ord(s[i]) + j) not in forbidden:
                    # 此位还能改
                    return genBeautifulStr(i, j)
                
        return ""
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestBeautifulString("dc", 4)) # ""
    print(solution.smallestBeautifulString("abcz", 26)) # "abda"
    print(solution.smallestBeautifulString("abcabcadc", 4)) # "abcabcdab"
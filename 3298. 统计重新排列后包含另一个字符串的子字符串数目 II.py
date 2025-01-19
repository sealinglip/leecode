# 给你两个字符串 word1 和 word2 。

# 如果一个字符串 x 重新排列后，word2 是重排字符串的前缀，那么我们称字符串 x 是 合法的 。
# 请你返回 word1 中 合法 子字符串的数目。
# 注意 ，这个问题中的内存限制比其他题目要 小 ，所以你 必须 实现一个线性复杂度的解法。


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
# 1 <= word1.length <= 10^6
# 1 <= word2.length <= 10^4
# word1 和 word2 都只包含小写英文字母。

from collections import Counter, defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # 用3297的解法测试用例1会TLE（本地跑不会）—— 要优化meetRequirement的处理
        stat = [0] * 26
        for c in word2:
            stat[ord(c) - ord('a')] -= 1

        res = 0
        n = len(word1)

        cnt = sum(1 for i in range(26) if stat[i] < 0)
        def update(i: int, delta: int) -> None:
            nonlocal cnt
            stat[i] += delta
            if stat[i] == 0 and delta > 0: # 说明之前 < 0
                cnt -= 1
            elif stat[i] == -1 and delta < 0: # 说明之前 == 0
                cnt += 1
        
        l = r = 0
        while r < n:
            while r < n and cnt > 0:
                update(ord(word1[r]) - ord('a'), 1)
                r += 1
            while l < r and cnt == 0:
                res += n - r + 1
                update(ord(word1[l]) - ord('a'), -1)
                l += 1

        return res
    
def load(filePath: str) -> str:
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception:
        return ""
    
if __name__ == "__main__":
    solution = Solution()
    # 488942635734
    print(solution.validSubstringCount(load("3298.word1.txt"), load("3298.word2.txt")))
    # 488729794967
    print(solution.validSubstringCount(load("3298.word3.txt"), load("3298.word4.txt")))
    print(solution.validSubstringCount("bcca", "abc")) # 1
    print(solution.validSubstringCount("abcabc", "abc")) # 10
    print(solution.validSubstringCount("abcabc", "aaabc")) # 0
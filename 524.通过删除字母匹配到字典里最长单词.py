#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，
# 该字符串可以通过删除 s 中的某些字符得到。
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。


# 示例 1：
# 输入：s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"]
# 输出："apple"

# 示例 2：
# 输入：s = "abpcplea", dictionary = ["a", "b", "c"]
# 输出："a"


# 提示：
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s 和 dictionary[i] 仅由小写英文字母组成

from typing import List
# @lc code=start


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 依次判断dictionary中的元素是不是s的子序列，是则记录长度
        maxLen, longestWord = 0, ""
        L = len(s)

        def isSubsequence(input: str) -> bool:
            '''
            双指针法来判断子序列
            '''
            p = 0
            nonlocal L
            for c in input:
                while p < L:
                    if s[p] == c:
                        p += 1
                        break
                    p += 1
                else:
                    return False

            return True

        for ca in dictionary:
            if len(ca) < maxLen:
                continue
            if isSubsequence(ca):
                if len(ca) > maxLen or ca < longestWord:
                    maxLen = len(ca)
                    longestWord = ca

        return longestWord

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLongestWord("abce",
                                   ["abe", "abc"]))  # "abc"
    print(solution.findLongestWord("abpcplea",
                                   ["ale", "apple", "monkey", "plea"]))  # "apple"
    print(solution.findLongestWord("abpcplea", ["a", "b", "c"]))  # "a"

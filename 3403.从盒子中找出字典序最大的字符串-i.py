#
# @lc app=leetcode.cn id=3403 lang=python3
#
# [3403] 从盒子中找出字典序最大的字符串 I
#
# https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/description/
#
# algorithms
# Medium (29.62%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 13.1K
# Testcase Example:  '"dbca"\n2'
#
# 给你一个字符串 word 和一个整数 numFriends。
# 
# Alice 正在为她的 numFriends 位朋友组织一个游戏。游戏分为多个回合，在每一回合中：
# word 被分割成 numFriends 个 非空 字符串，且该分割方式与之前的任意回合所采用的都 不完全相同 。
# 所有分割出的字符串都会被放入一个盒子中。
# 
# 在所有回合结束后，找出盒子中 字典序最大的 字符串。
# 
# 
# 示例 1：
# 输入: word = "dbca", numFriends = 2
# 输出: "dbc"
# 解释: 
# 所有可能的分割方式为：
# "d" 和 "bca"。
# "db" 和 "ca"。
# "dbc" 和 "a"。
# 
# 示例 2：
# 输入: word = "gggg", numFriends = 4
# 输出: "g"
# 解释: 
# 唯一可能的分割方式为："g", "g", "g", 和 "g"。
# 
# 
# 提示:
# 1 <= word.length <= 5 * 10^3
# word 仅由小写英文字母组成。
# 1 <= numFriends <= word.length
# 
# 

# @lc code=start
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        maxLen = len(word) - numFriends + 1 # 分隔的最大长度
        # 构建映射表
        d = [[] for _ in range(26)]
        base = ord('a')
        for i, c in enumerate(word):
            d[ord(c) - base].append(i)
        
        arr = None
        for i in range(25, -1, -1):
            if d[i]:
                arr = d[i]
                break

        res = ""
        n = len(word)
        while arr:
            res += word[arr[0]]
            if len(res) == maxLen:
                break
            newArr = None
            ma = ' '
            for i in arr:
                i += 1
                if i < n:
                    if word[i] > ma:
                        ma = word[i]
                        newArr = [i]
                    elif word[i] == ma:
                        newArr.append(i)
            arr = newArr

        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.answerString("jcooek", 4)) # "ooe"
    print(solution.answerString("gh", 1)) # "gh"
    print(solution.answerString("dbca", 2)) # "dbc"
    print(solution.answerString("gggg", 4)) # "g"

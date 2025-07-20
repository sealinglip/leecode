#
# @lc app=leetcode.cn id=3330 lang=python3
#
# [3330] 找到初始输入字符串 I
#
# https://leetcode.cn/problems/find-the-original-typed-string-i/description/
#
# algorithms
# Easy (69.22%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 17.6K
# Testcase Example:  '"abbcccc"'
#
# Alice 正在她的电脑上输入一个字符串。但是她打字技术比较笨拙，她 可能 在一个按键上按太久，导致一个字符被输入 多次 。
# 尽管 Alice 尽可能集中注意力，她仍然可能会犯错 至多 一次。
# 给你一个字符串 word ，它表示 最终 显示在 Alice 显示屏上的结果。
# 请你返回 Alice 一开始可能想要输入字符串的总方案数。
# 
# 
# 示例 1：
# 输入：word = "abbcccc"
# 输出：5
# 解释：
# 可能的字符串包括："abbcccc" ，"abbccc" ，"abbcc" ，"abbc" 和 "abcccc" 。
# 
# 示例 2：
# 输入：word = "abcd"
# 输出：1
# 解释：
# 唯一可能的字符串是 "abcd" 。
# 
# 示例 3：
# 输入：word = "aaaa"
# 输出：4
# 
# 
# 提示：
# 1 <= word.length <= 100
# word 只包含小写英文字母。
# 
# 复习

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        # 方法1：
        # res = 1
        # repeat = 1
        # prev = word[0]
        # for c in word[1:]:
        #     if c != prev:
        #         res += repeat - 1
        #         repeat = 1
        #         prev = c
        #     else:
        #         repeat += 1
        # res += repeat - 1

        # return res
        
        # 方法2：
        res = 1
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                res += 1
        return res
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleStringCount("abbcccc")) # 5
    print(solution.possibleStringCount("abcd")) # 1
    print(solution.possibleStringCount("aaaa")) # 4

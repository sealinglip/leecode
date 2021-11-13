#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#
# 我们定义，在以下情况时，单词的大写用法是正确的：

# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。


# 示例 1：
# 输入：word = "USA"
# 输出：true

# 示例 2：
# 输入：word = "FlaG"
# 输出：false


# 提示：
# 1 <= word.length <= 100
# word 由小写和大写英文字母组成

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return False
        L = len(word)
        if L == 1:
            return True
        firstUppercase = word[0].isupper()
        secondUppercase = word[1].isupper()
        if firstUppercase and secondUppercase:
            # 后续必须都是大写才合规
            return all([c.isupper() for c in word[2:]])
        elif secondUppercase:
            return False
        else:
            # 后续必须都是小写
            return all([c.islower() for c in word[2:]])


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.detectCapitalUse("mL"))

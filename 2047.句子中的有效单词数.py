#
# @lc app=leetcode.cn id=2047 lang=python3
#
# [2047] 句子中的有效单词数
#
# 句子仅由小写字母（'a' 到 'z'）、数字（'0' 到 '9'）、连字符（'-'）、标点符号（'!'、'.' 和 ','）以及空格（' '）组成。每个句子可以根据空格分解成 一个或者多个 token ，这些 token 之间由一个或者多个空格 ' ' 分隔。

# 如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：

# 仅由小写字母、连字符和/或标点（不含数字）。
# 至多一个 连字符 '-' 。如果存在，连字符两侧应当都存在小写字母（"a-b" 是一个有效单词，但 "-ab" 和 "ab-" 不是有效单词）。
# 至多一个 标点符号。如果存在，标点符号应当位于 token 的 末尾 。
# 这里给出几个有效单词的例子："a-b."、"afad"、"ba-c"、"a!" 和 "!" 。

# 给你一个字符串 sentence ，请你找出并返回 sentence 中 有效单词的数目 。


# 示例 1：
# 输入：sentence = "cat and  dog"
# 输出：3
# 解释：句子中的有效单词是 "cat"、"and" 和 "dog"

# 示例 2：
# 输入：sentence = "!this  1-s b8d!"
# 输出：0
# 解释：句子中没有有效单词
# "!this" 不是有效单词，因为它以一个标点开头
# "1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字

# 示例 3：
# 输入：sentence = "alice and  bob are playing stone-game10"
# 输出：5
# 解释：句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"
# "stone-game10" 不是有效单词，因为它含有数字

# 示例 4：
# 输入：sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
# 输出：6
# 解释：句子中的有效单词是 "he"、"bought"、"pencils,"、"erasers,"、"and" 和 "pencil-sharpener."


# 提示：
# 1 <= sentence.length <= 1000
# sentence 由小写英文字母、数字（0-9）、以及字符（' '、'-'、'!'、'.' 和 ','）组成
# 句子中至少有 1 个 token

# @lc code=start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        # Deterministic finite automaton (DFA, 确定有穷状态自动机)
        # 状态转移表
        # state letter  digit blank  -  !.,
        # 0     1       2     0      2  4
        # 1     1       2     0      3  4
        # 2     2       2     0      2  2
        # 3     5       2     0      2  2
        # 4     2       2     0      2  2
        # 5     5       2     0      2  4

        # 从1、4、5变到0，计数+1，退出循环时状态为1、4、5亦加1
        transfer = [[1, 2, 0, 2, 4],
                    [1, 2, 0, 3, 4],
                    [2, 2, 0, 2, 2],
                    [5, 2, 0, 2, 2],
                    [2, 2, 0, 2, 2],
                    [5, 2, 0, 2, 4]]

        def type(c: str) -> int:  # 将字符转换为类型
            if c == ' ':
                return 2
            elif '9' >= c >= '0':
                return 1
            elif 'z' >= c >= 'a':
                return 0
            elif '-' == c:
                return 3
            else:
                return 4

        state = 0
        res = 0

        for c in sentence:
            newState = transfer[state][type(c)]
            if newState == 0 and (state == 1 or state == 4 or state == 5):
                res += 1
            state = newState

        if state == 1 or state == 4 or state == 5:
            res += 1

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countValidWords("!"))  # 1
    print(solution.countValidWords("cat and  dog"))  # 3
    print(solution.countValidWords("!this  1-s b8d!"))  # 0
    print(solution.countValidWords("alice and  bob are playing stone-game10"))  # 5
    print(solution.countValidWords(
        "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))  # 6

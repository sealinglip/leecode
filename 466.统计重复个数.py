#
# @lc app=leetcode.cn id=466 lang=python3
#
# [466] 统计重复个数
#
# 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。

# 例如，str == ["abc", 3] =="abcabcabc" 。
# 如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。

# 例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。
# 现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, n2] 。

# 请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。
 
# 示例 1：
# 输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# 输出：2

# 示例 2：
# 输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# 输出：1
 
# 提示：
# 1 <= s1.length, s2.length <= 100
# s1 和 s2 由小写英文字母组成
# 1 <= n1, n2 <= 10^6

# Hard
# 复习

# @lc code=start
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 找出最小循环节
        l2 = len(s2)
        c1 = c2 = i = 0 # s1的个数、s2的个数和s2当前待匹配的索引
        idxMap = {}
        while True:
            for c in s1:
                if c == s2[i]:
                    i += 1
                    if i == l2:
                        c2, i = c2 + 1, 0 #新一轮
            c1 += 1 # 又遍历了一个s1
            
            if c1 == n1:
                # s1 已经用完了，当前匹配了c2个s2，也就是(c2 // n2)个str2
                return c2 // n2
            
            if i in idxMap:
                # 之前出现过i，说明找到了循环节
                break
            else:
                idxMap[i] = (c1, c2)

        # 前preC1个s1中包含了preC2个s2    
        preC1, preC2 = idxMap[i]
        # 之后的每个loop[0]个s1中包含了loop[1]个s2
        loop = (c1 - preC1, c2 - preC2) # 循环节
        # total记录str1包含的s2的数量
        total = preC2 + (n1 - preC1) // loop[0] * loop[1]
        # str1还剩余一些尾巴，需要处理
        rest = (n1 - preC1) % loop[0] # 剩下的s1
        for _ in range(rest):
            for c in s1:
                if c == s2[i]:
                    i += 1
                    if i == l2:
                        total, i = total + 1, 0

        return total // n2

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.getMaxRepetitions("aaa", 3, "aa", 1)) # 4
    print(solution.getMaxRepetitions("acb", 4, "ab", 2)) # 2
    print(solution.getMaxRepetitions("acb", 4, "abab", 2)) # 1
    print(solution.getMaxRepetitions("acb", 1, "acb", 1)) # 1
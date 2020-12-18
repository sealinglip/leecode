#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true

# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false

# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false

# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 

# @lc code=start
import re
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern:
            return not s
        elif not s:
            return False
        else:
            parts = re.split("\\s+", s)
            if len(pattern) != len(parts):
                return False
            
            mapping = {}
            reverseMapping = {}
            for c, p in zip(pattern, parts):
                if c in mapping:
                    if p != mapping[c]:
                        return False
                elif p in reverseMapping:
                    return False
                else:
                    mapping[c] = p
                    reverseMapping[p] = c
            return True

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog cat cat fish"))
    print(solution.wordPattern("aaaa", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog dog dog dog"))
#
# @lc app=leetcode.cn id=2645 lang=python3
#
# [2645] 构造有效字符串的最少插入数
#
# 给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。

# 如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。

 
# 示例 1：
# 输入：word = "b"
# 输出：2
# 解释：在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "abc" 。

# 示例 2：
# 输入：word = "aaa"
# 输出：6
# 解释：在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "abcabcabc" 。

# 示例 3：
# 输入：word = "abc"
# 输出：0
# 解释：word 已经是有效字符串，不需要进行修改。 
 

# 提示：
# 1 <= word.length <= 50
# word 仅由字母 "a"、"b" 和 "c" 组成。

# @lc code=start
class Solution:
    def addMinimum(self, word: str) -> int:
        def expectNext(cur: str):
            return 'a' if cur == 'c' else ('b' if cur == 'a' else 'c')
        
        expected = 'a' # 期望的下一个字符
        res = 0
        for c in word:
            while c != expected:
                expected = expectNext(expected)
                res += 1
            expected = expectNext(expected)

        # 末尾补齐
        if word[-1] != 'c':
            res += 1 if word[-1] == 'b' else 2
            
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.addMinimum("b")) # 2
    print(solution.addMinimum("aaa")) # 6
    print(solution.addMinimum("abc")) # 0
#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#
# 给你一个字符串 s，最多 可以从中删除一个字符。
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。


# 示例 1：
# 输入：s = "aba"
# 输出：true

# 示例 2：
# 输入：s = "abca"
# 输出：true
# 解释：你可以删除字符 'c' 。

# 示例 3：
# 输入：s = "abc"
# 输出：false
 

# 提示：
# 1 <= s.length <= 10^5
# s 由小写英文字母组成

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l: int, r: int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
                    
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return check(l+1, r) or check(l, r-1)
        return True
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.validPalindrome("aba")) # True
    print(solution.validPalindrome("abca")) # True
    print(solution.validPalindrome("abc")) # False

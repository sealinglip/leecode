#
# @lc app=leetcode.cn id=1745 lang=python3
#
# [1745] 分割回文串 IV
#
# 给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。

# 当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。

 

# 示例 1：
# 输入：s = "abcbdd"
# 输出：true
# 解释："abcbdd" = "a" + "bcb" + "dd"，三个子字符串都是回文的。

# 示例 2：
# 输入：s = "bcbddxy"
# 输出：false
# 解释：s 没办法被分割成 3 个回文子字符串。
 

# 提示：
# 3 <= s.length <= 2000
# s​​​​​​ 只包含小写英文字母。

# Hard
# @lc code=start
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)] # isPalindrome[i][j] 记录s[i:j+1]是否回文串
        for span in range(1, n):
            for i in range(n-span+1):
                j = i + span - 1
                if span == 1:
                    isPalindrome[i][j] = True
                elif span == 2:
                    isPalindrome[i][j] = s[i] == s[j]
                else:
                    isPalindrome[i][j] = isPalindrome[i+1][j-1] and (s[i] == s[j])

        for i in range(n-2):
            if not isPalindrome[0][i]:
                continue
            for j in range(i+1, n-1):
                if isPalindrome[i+1][j] and isPalindrome[j+1][n-1]:
                    return True
        
        return False

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPartitioning("abcbdd")) # True
    print(solution.checkPartitioning("bcbddxy")) # False

#
# @lc app=leetcode.cn id=2609 lang=python3
#
# [2609] 最长平衡子字符串
#
# 给你一个仅由 0 和 1 组成的二进制字符串 s 。  

# 如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。 

# 返回  s 中最长的平衡子字符串长度。

# 子字符串是字符串中的一个连续字符序列。

 

# 示例 1：
# 输入：s = "01000111"
# 输出：6
# 解释：最长的平衡子字符串是 "000111" ，长度为 6 。

# 示例 2：
# 输入：s = "00111"
# 输出：4
# 解释：最长的平衡子字符串是 "0011" ，长度为  4 。

# 示例 3：
# 输入：s = "111"
# 输出：0
# 解释：除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
 

# 提示：
# 1 <= s.length <= 50
# '0' <= s[i] <= '1'

# 复习

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # 记连续0 和连续1
        consec0 = consec1 = res = 0
        prev = '2'

        for c in s:
            if c == prev:
                if c == '0':
                    consec0 += 1
                else:
                    consec1 += 1
            else:
                if c == '0':
                    res = max(res, min(consec0, consec1) << 1)
                    consec0 = 1
                    consec1 = 0
                else:
                    consec1 = 1

            prev = c

        res = max(res, min(consec0, consec1) << 1)
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheLongestBalancedSubstring("01000111")) # 6
    print(solution.findTheLongestBalancedSubstring("00111")) # 4
    print(solution.findTheLongestBalancedSubstring("111")) # 0
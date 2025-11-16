#
# @lc app=leetcode.cn id=3234 lang=python3
#
# [3234] 统计 1 显著的字符串的数量
#
# https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones/description/
#
# algorithms
# Medium (27.21%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    7.1K
# Total Submissions: 20.3K
# Testcase Example:  '"00011"'
#
# 给你一个二进制字符串 s。
# 请你统计并返回其中 1 显著  的 子字符串 的数量。
# 如果字符串中 1 的数量 大于或等于 0 的数量的 平方，则认为该字符串是一个 1 显著 的字符串 。
# 
# 
# 示例 1：
# 输入：s = "00011"
# 输出：5
# 解释：
# 1 显著的子字符串如下表所示。
# i  j   s[i..j]   0 的数量    1 的数量
# 3  3   1         0          1
# 4  4   1         0          1
# 2  3   01        1          1
# 3  4   11        0          2
# 2  4   011       1          2
# 
# 示例 2：
# 输入：s = "101101"
# 输出：16
# 解释：
# 1 不显著的子字符串如下表所示。
# 总共有 21 个子字符串，其中 5 个是 1 不显著字符串，因此有 16 个 1 显著子字符串。
# i  j   s[i..j]   0 的数量    1 的数量
# 1  1   0         1          0
# 4  4   0         1          0
# 1  4   0110      2          2
# 0  4   10110     2          3
# 1  5   01101     2          3
# 
# 
# 提示：
# 1 <= s.length <= 4 * 10^4
# s 仅包含字符 '0' 和 '1'。
# 
# 复习
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n+1) # pre[j]记录位置j之前最近的0的位置
        for i in range(n):
            if i == 0 or s[i-1] == '0':
                pre[i+1] = i
            else:
                pre[i+1] = pre[i]

        res = 0
        for r in range(1, n+1):
            cnt0 = int(s[r-1] == '0') # 以r为右界开始对0计数
            l = r
            while l > 0 and cnt0 * cnt0 <= n:
                cnt1 = (r - pre[l]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(l - pre[l], cnt1 - cnt0 * cnt0 + 1)
                l = pre[l]
                cnt0 += 1
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubstrings("00011")) # 5
    print(solution.numberOfSubstrings("101101")) # 16
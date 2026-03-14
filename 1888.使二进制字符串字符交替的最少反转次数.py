#
# @lc app=leetcode.cn id=1888 lang=python3
#
# [1888] 使二进制字符串字符交替的最少反转次数
#
# https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/
#
# algorithms
# Medium (41.49%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 37.5K
# Testcase Example:  '"111000"'
#
# 给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：
# 类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
# 类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
# 
# 请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。
# 我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。
# 
# 比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
# 
# 
# 示例 1：
# 输入：s = "111000"
# 输出：2
# 解释：执行第一种操作两次，得到 s = "100011" 。
# 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
# 
# 示例 2：
# 输入：s = "010"
# 输出：0
# 解释：字符串已经是交替的。
# 
# 示例 3：
# 输入：s = "1110"
# 输出：1
# 解释：对第二个字符执行第二种操作，得到 s = "1010" 。
# 
# 
# 提示：
# 1 <= s.length <= 10^5
# s[i] 要么是 '0' ，要么是 '1' 。
# 
# 
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        # 先统计分布
        odd1s = odd0s = even1s = even0s = 0
        for i in range(n):
            if s[i] == '1':
                if i & 1:
                    odd1s += 1
                else:
                    even1s += 1
            elif i & 1:
                odd0s += 1
            else:
                even0s += 1

        # 如果长度为偶数，类型1操作确实会互换odd1s & odd0s 和 even1s & even0s
        # 但也不会改变对类型2操作的需求
        # 直接判断最少要多少次类型2操作即可
        if n & 1 == 0:
            return min(odd1s + even0s, odd0s + even1s)
        # 如果长度为奇数，类型1操作会改变奇数位和偶数位的数字构成
        else:
            res = min(odd1s + even0s, odd0s + even1s)
            for i in range(n-1):
                delta0 = 1 if s[i] == '0' else 0
                delta1 = 1 if s[i] == '1' else 0
                odd0s, odd1s, even0s, even1s = even0s - delta0, even1s - delta1, odd0s + delta0, odd1s + delta1
                res = min(res, odd1s + even0s, odd0s + even1s)
                
            return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minFlips("01001001101")) # 2
    print(solution.minFlips("111000")) # 2
    print(solution.minFlips("010")) # 0
    print(solution.minFlips("1110")) # 1
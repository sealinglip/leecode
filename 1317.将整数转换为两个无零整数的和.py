#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#
# https://leetcode.cn/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/
#
# algorithms
# Easy (62.71%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 35.3K
# Testcase Example:  '2'
#
# 「无零整数」是十进制表示中 不含任何 0 的正整数。
# 给你一个整数 n，请你返回一个 由两个整数组成的列表 [a, b]，满足：
# a 和 b 都是无零整数
# a + b = n
# 
# 题目数据保证至少有一个有效的解决方案。
# 如果存在多个有效解决方案，你可以返回其中任意一个。
# 
# 
# 示例 1：
# 输入：n = 2
# 输出：[1,1]
# 解释：a = 1, b = 1。a + b = n 并且 a 和 b 的十进制表示形式都不包含任何 0。
# 
# 示例 2：
# 输入：n = 11
# 输出：[2,9]
# 
# 示例 3：
# 输入：n = 10000
# 输出：[1,9999]
# 
# 示例 4：
# 输入：n = 69
# 输出：[1,68]
# 
# 示例 5：
# 输入：n = 1010
# 输出：[11,999]
# 
# 
# 提示：
# 2 <= n <= 10^4
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        s = str(n)[::-1]
        i = borrow = 0
        l = len(s)
        a = []
        minALen = 0 
        while i < l:
            d = int(s[i]) # 当前数位转成数字
            if borrow:
                if d == 0:
                    d = 9
                    minALen = i
                else:
                    d -= borrow
                    borrow = 0
            if i == l-1 and d == 0:
                # 最后一位了，只剩0了，可以不处理了
                continue
            if not a or d == 0:
                # 当前位必须拆，那么a的最小长度必须到这一位
                minALen = i+1

            # 拆分
            if d < 2:
                a.append(str(d+1))
                borrow = 1
            else:
                a.append('1')

            i += 1
        
        n1 = int("".join(a[:minALen][::-1]))
        return [n1, n-n1]

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.getNoZeroIntegers(5012)) # [21,4991]
    print(solution.getNoZeroIntegers(2)) # [1,1]
    print(solution.getNoZeroIntegers(11)) # [2,9]
    print(solution.getNoZeroIntegers(10000)) # [1,9999]
    print(solution.getNoZeroIntegers(69)) # [1,68]
    print(solution.getNoZeroIntegers(1010)) # [11,999]
    print(solution.getNoZeroIntegers(1011)) # [12,999]
    print(solution.getNoZeroIntegers(12011)) # [12,11999]

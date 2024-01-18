#
# @lc app=leetcode.cn id=2719 lang=python3
#
# [2719] 统计整数数目
#
# 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：

# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# 请你返回好整数的数目。答案可能很大，请返回答案对 10^9 + 7 取余后的结果。

# 注意，digit_sum(x) 表示 x 各位数字之和。


# 示例 1：
# 输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
# 输出：11
# 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。

# 示例 2：
# 输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
# 输出：5
# 解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
 

# 提示：
# 1 <= num1 <= num2 <= 10^22
# 1 <= min_sum <= max_sum <= 400

# Hard
# 复习

# @lc code=start
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        # 之所以前两个参数为字符串，就是它可能为超限
        # 记dp(n) = count(min_sum <= digit_sum(i) <= max_sum for i in range(n))
        # 本题答案为 dp(num2) - dp(num1 - 1)

        def decrease(num: str) -> str:
            '''
            将数减一返回
            '''
            digits = list(num)
            i = len(digits) - 1
            while digits[i] == '0':
                i -= 1
            
            digits[i] = chr(ord(digits[i]) - 1)
            i += 1
            for j in range(i, len(digits)):
                digits[j] = '9'

            return ''.join(digits)
        
        def dfs(num: str, i: int, j: int, limit: bool) -> int:
            '''
            i: 当前最高位
            '''
            if j > max_sum:
                return 0
            if i == -1:
                return j >= min_sum
            
            if not limit and d[i][j] != -1:
                return d[i][j]
            res = 0
            up = ord(num[i]) - ord('0') if limit else 9
            for x in range(up + 1):
                res = (res + dfs(num, i - 1, j + x, limit and x == up)) % MOD

            if not limit:
                d[i][j] = res
            return res
            
        
        def dp(num: str) -> int:
            return dfs(num[::-1], len(num) - 1, 0, True)
        
        N, M = 23, 401
        d = [[-1] * M for _ in range(N)]
        return (dp(num2) - dp(decrease(num1)) + MOD) % MOD


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.count("1", "12", 1, 8)) # 11
    print(solution.count("1", "5", 1, 5)) # 5
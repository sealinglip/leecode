#
# @lc app=leetcode.cn id=2844 lang=python3
#
# [2844] 生成特殊数字的最少操作
#
# 给你一个下标从 0 开始的字符串 num ，表示一个非负整数。
# 在一次操作中，您可以选择 num 的任意一位数字并将其删除。请注意，如果你删除 num 中的所有数字，则 num 变为 0。
# 返回最少需要多少次操作可以使 num 变成特殊数字。
# 如果整数 x 能被 25 整除，则该整数 x 被认为是特殊数字。

# 示例 1：
# 输入：num = "2245047"
# 输出：2
# 解释：删除数字 num[5] 和 num[6] ，得到数字 "22450" ，可以被 25 整除。
# 可以证明要使数字变成特殊数字，最少需要删除 2 位数字。

# 示例 2：
# 输入：num = "2908305"
# 输出：3
# 解释：删除 num[3]、num[4] 和 num[6] ，得到数字 "2900" ，可以被 25 整除。
# 可以证明要使数字变成特殊数字，最少需要删除 3 位数字。

# 示例 3：
# 输入：num = "10"
# 输出：1
# 解释：删除 num[0] ，得到数字 "0" ，可以被 25 整除。
# 可以证明要使数字变成特殊数字，最少需要删除 1 位数字。
 

# 提示
# 1 <= num.length <= 100
# num 仅由数字 '0' 到 '9' 组成
# num 不含任何前导零

# @lc code=start
from math import inf


class Solution:
    def minimumOperations(self, num: str) -> int:
        # 能被25整除，那么末尾只能是四种可能：25/50/75/00，或者数就是0
        # 所有从尾巴往前找，找最短匹配模式，如果找不到，那就只能取0（全删，或者剩个0）
        # 把num翻转，那就是从前往后找
        n = len(num)
        num = num[::-1]

        def findPattern(first: str, second: str) -> int:
            '''
            返回匹配模式的最短前缀长度，如果未匹配，返回inf
            '''
            idx = num.find(first)
            patternLen = inf
            if idx != -1:
                idx += 1
                for s in second:
                    idx2 = num.find(s, idx)
                    if idx2 != -1:
                        patternLen = min(patternLen, idx2+1)
            return patternLen

        l = min(findPattern('5', '27'), findPattern('0', '05'))
        return (n if num.find('0') == -1 else n-1) if l == inf else l - 2
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumOperations("2245047")) # 2
    print(solution.minimumOperations("2908305")) # 3
    print(solution.minimumOperations("10")) # 1
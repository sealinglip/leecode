#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。


# 示例 1：
# 输入： "()"
# 输出： 1

# 示例 2：
# 输入： "(())"
# 输出： 2

# 示例 3：
# 输入： "()()"
# 输出： 2

# 示例 4：
# 输入： "(()(()))"
# 输出： 6


# 提示：
# S 是平衡括号字符串，且只含有(和) 。
# 2 <= S.length <= 50

# 复习

from collections import defaultdict
# @lc code=start


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # scorePerDepth = defaultdict(int)
        # depth = 0
        # for c in s:
        #     if c == '(':
        #         cur = scorePerDepth[depth]
        #         if cur:  # 之前有并列的平衡括号字符串
        #             pass
        #         else:
        #             scorePerDepth[depth] = -1
        #         depth += 1
        #     else:
        #         cur = abs(scorePerDepth[depth])
        #         scorePerDepth[depth] = 0  # 清空
        #         depth -= 1
        #         if cur:
        #             if scorePerDepth[depth] == -1:
        #                 scorePerDepth[depth] = cur * 2
        #             else:
        #                 scorePerDepth[depth] += cur * 2
        #         else:
        #             if scorePerDepth[depth] == -1:
        #                 scorePerDepth[depth] = 1
        #             else:
        #                 scorePerDepth[depth] += 1

        # return abs(scorePerDepth[0])

        # 方法2：栈
        # 我们把平衡字符串 s 看作是一个空字符串加上 s 本身，并且定义空字符串的分数为 0。使用栈 st 记录平衡字符串的分数，在开始之前要压入分数 0，表示空字符串的分数。

        # 在遍历字符串 s 的过程中：
        # 遇到左括号，那么我们需要计算该左括号内部的子平衡括号字符串 A 的分数，我们也要先压入分数 0，表示 A 前面的空字符串的分数。
        # 遇到右括号，说明该右括号内部的子平衡括号字符串 A 的分数已经计算出来了，我们将它弹出栈，并保存到变量 v 中。如果 v = 0，那么说明子平衡括号字符串 A 是空串，(A) 的分数为 1，
        # 否则(A)的分数为 2v，然后将(A) 的分数加到栈顶元素上。
        # 遍历结束后，栈顶元素保存的就是 s 的分数。
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(2 * v, 1)
        return st[-1]

        # 方法3：这个方法巧
        # 根据题意，s 的分数与 1 分的() 有关。对于每个()，它的最终分数与它所处的深度有关，如果深度为 depth，那么它的最终分数为 2 ^ depth。我们统计所有() 的最终分数和即可。
        # res = depth = 0
        # for i, c in enumerate(s):
        #     depth += 1 if c == '(' else -1
        #     if c == ')' and s[i - 1] == '(':
        #         res += 1 << depth

        # return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.scoreOfParentheses("()"))  # 1
    print(solution.scoreOfParentheses("(())"))  # 2
    print(solution.scoreOfParentheses("()()"))  # 2
    print(solution.scoreOfParentheses("(()(()))"))  # 6
    print(solution.scoreOfParentheses("(()(())(()))"))  # 10
    print(solution.scoreOfParentheses("(()(()())(()))"))  # 14

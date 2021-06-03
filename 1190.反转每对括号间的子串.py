#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。

# 示例 1：
# 输入：s = "(abcd)"
# 输出："dcba"

# 示例 2：
# 输入：s = "(u(love)i)"
# 输出："iloveu"

# 示例 3：
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"

# 示例 4：
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == "(":
                stack.append([])
            elif c == ")":
                arr = stack.pop()
                arr.reverse()
                stack[-1].extend(arr)
            else:
                stack[-1].append(c)

        return "".join(stack[-1])


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseParentheses("(abcd)"))
    print(solution.reverseParentheses("(u(love)i)"))
    print(solution.reverseParentheses("(ed(et(oc))el)"))
    print(solution.reverseParentheses("a(bcdefghijkl(mno)p)q"))

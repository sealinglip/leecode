#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
# 返回所有可能的结果。答案可以按 任意顺序 返回。


# 示例 1：
# 输入：s = "()())()"
# 输出：["(())()", "()()()"]

# 示例 2：
# 输入：s = "(a)())()"
# 输出：["(a())()", "(a)()()"]

# 示例 3：
# 输入：s = ")("
# 输出：[""]


# 提示：
# 1 <= s.length <= 25
# s 由小写英文字母以及括号 '(' 和 ')' 组成
# s 中至多含 20 个括号

# Hard

from typing import List
# @lc code=start


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lExcess, rExcess = 0, 0  # 记录整个字符串中需要删除的左括号和右括号数
        for c in s:
            if c == '(':
                lExcess += 1
            elif c == ')':
                if lExcess > 0:
                    lExcess -= 1
                else:
                    rExcess += 1

        def isValid(txt: str) -> bool:
            '''
            判断是否为有效字符串
            '''
            lCnt = 0
            for c in txt:
                if c == '(':
                    lCnt += 1
                elif c == ')':
                    if lCnt > 0:
                        lCnt -= 1
                    else:
                        return False
            return lCnt == 0

        res = []

        def findSolution(txt: str, start: int, lCnt: int, rCnt: int, lDel: int, rDel: int) -> None:
            '''
            尝试修复txt字符串
            txt: 待修复
            start: 尝试的起始位置(假定txt[:start]已经是有效子串)
            lCnt: start位置之前已经累计的左括号数
            rCnt: start位置之前已经累计的右括号数
            lDel: 待删除的左括号数
            rDel: 待删除的右括号数
            '''
            if lDel + rDel == 0:
                if isValid(txt):
                    res.append(txt)
                return

            L = len(txt)
            for i in range(start, L):
                if i > start and txt[i] == txt[i - 1]:
                    # 对于连续重复的字符，在第一个位置处就已经尝试过了，不需要重复尝试
                    if txt[i] == '(':
                        lCnt += 1
                    elif txt[i] == ')':
                        rCnt += 1
                    continue

                if L - i < lDel + rDel:
                    # 剩余字符数不够删的
                    return
                if txt[i] == '(':
                    if lDel > 0:
                        # 尝试着干掉它试试
                        findSolution(txt[:i] + txt[i+1:], i,
                                     lCnt, rCnt, lDel-1, rDel)
                    # 放过它，试后面的
                    lCnt += 1
                elif txt[i] == ')':
                    if rDel > 0:
                        # 尝试干掉它试试
                        findSolution(txt[:i] + txt[i+1:], i,
                                     lCnt, rCnt, lDel, rDel-1)
                    # 放过
                    rCnt += 1
                if rCnt > lCnt:
                    # 已经不可能有效了
                    return

        findSolution(s, 0, 0, 0, lExcess, rExcess)

        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeInvalidParentheses(
        "(r(()()("))  # ["r()()","r(())","(r)()","(r())"]
    # print(solution.removeInvalidParentheses(")("))  # [""]
    # print(solution.removeInvalidParentheses("()())()"))  # ["(())()","()()()"]
    # print(solution.removeInvalidParentheses("(a)())()")
    #       )  # ["(a())()","(a)()()"]

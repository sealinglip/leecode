#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode.cn/problems/24-game/description/
#
# algorithms
# Hard (53.88%)
# Likes:    486
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 89.7K
# Testcase Example:  '[4,1,8,7]'
#
# 给定一个长度为4的整数数组 cards 。你有 4 张卡片，每张卡片上都包含一个范围在 [1,9] 的数字。您应该使用运算符 ['+', '-',
# '*', '/'] 和括号 '(' 和 ')' 将这些卡片上的数字排列成数学表达式，以获得值24。
# 
# 你须遵守以下规则:
# 除法运算符 '/' 表示实数除法，而不是整数除法。
# 
# 例如， 4 /(1 - 2 / 3)= 4 /(1 / 3)= 12 。
# 
# 每个运算都在两个数字之间。特别是，不能使用 “-” 作为一元运算符。
# 例如，如果 cards =[1,1,1,1] ，则表达式 “-1 -1 -1 -1” 是 不允许 的。
# 
# 你不能把数字串在一起
# 例如，如果 cards =[1,2,1,2] ，则表达式 “12 + 12” 无效。
# 
# 
# 如果可以得到这样的表达式，其计算结果为 24 ，则返回 true ，否则返回 false 。
# 
# 
# 示例 1:
# 输入: cards = [4, 1, 8, 7]
# 输出: true
# 解释: (8-4) * (7-1) = 24
# 
# 示例 2:
# 输入: cards = [1, 2, 1, 2]
# 输出: false
# 
# 
# 提示:
# cards.length == 4
# 1 <= cards[i] <= 9
# 
#

from typing import List
# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(cards)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.judgePoint24([4, 1, 8, 7])) # True
    print(solution.judgePoint24([1, 2, 1, 2])) # False

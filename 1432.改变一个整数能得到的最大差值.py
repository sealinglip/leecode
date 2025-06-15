#
# @lc app=leetcode.cn id=1432 lang=python3
#
# [1432] 改变一个整数能得到的最大差值
#
# https://leetcode.cn/problems/max-difference-you-can-get-from-changing-an-integer/description/
#
# algorithms
# Medium (40.33%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 30.9K
# Testcase Example:  '555'
#
# 给你一个整数 num 。你可以对它进行以下步骤共计 两次：
# 
# 选择一个数字 x (0 <= x <= 9).
# 选择另一个数字 y (0 <= y <= 9) 。数字 y 可以等于 x 。
# 将 num 中所有出现 x 的数位都用 y 替换。
# 
# 令两次对 num 的操作得到的结果分别为 a 和 b 。
# 请你返回 a 和 b 的 最大差值 。
# 注意，新的整数（a 或 b）必须不能 含有前导 0，并且 非 0。
# 
# 
# 示例 1：
# 输入：num = 555
# 输出：888
# 解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
# 第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
# 现在，我们有 a = 999 和 b = 111 ，最大差值为 888
# 
# 示例 2：
# 输入：num = 9
# 输出：8
# 解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
# 第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
# 现在，我们有 a = 9 和 b = 1 ，最大差值为 8
# 
# 示例 3：
# 输入：num = 123456
# 输出：820000
# 
# 示例 4：
# 输入：num = 10000
# 输出：80000
# 
# 示例 5：
# 输入：num = 9288
# 输出：8700
# 
# 
# 提示：
# 1 <= num <= 10^8
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        ma = mi = s
        for c in s:
            if c != '9':
                ma = s.replace(c, '9')
                break
        first = s[0]
        if first != '1':
            mi = s.replace(first, '1')
        else:
            for c in s:
                if c != '0' and c != first:
                    mi = s.replace(c, '0')
                    break
        return int(ma) - int(mi)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDiff(1101057)) # 8808050
    print(solution.maxDiff(555)) # 888
    print(solution.maxDiff(9)) # 8
    print(solution.maxDiff(123456)) # 820000
    print(solution.maxDiff(10000)) # 80000
    print(solution.maxDiff(9288)) # 8700

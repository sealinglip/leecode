#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#
# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？


# 示例：
# 输入: 10
# 输出: 4
# 解释:
# 在[1, 10]中有四个好数： 2, 5, 6, 9。
# 注意 1 和 10 不是好数, 因为他们在旋转之后不变。


# 提示：
# N 的取值范围是[1, 10000]。

# 复习

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        def getLegal(digits: int, lead: int, limit: bool) -> int:
            '''
            digits: 位数(含首位)
            lead: 首位
            limit: 是否限制必须有2，5，6，9出现
            '''
            res = 0
            a, b = 7 ** (digits - 1) - 3 ** (digits - 1), 7 ** (digits - 1)
            for i in range(lead if digits > 1 else (lead + 1)):
                if i == 0 or i == 1 or i == 8:
                    res += a if limit else b
                elif i == 2 or i == 5 or i == 6 or i == 9:
                    res += b
            return res

        # 满足条件的数字只能由0、1、2、5、6、8、9组成，且必须包含2、5、6、9中的至少一个
        # N位数中总共有多少个这样的数呢？
        # 旋转后还有效的数字 - 旋转后等于自身的数字
        # 6 * (7 ^ (N - 1)) - 2 * (3 ^ (N - 1))
        num = str(n)
        N = len(num)  # N位数
        res = 0

        limit = True
        for i, c in enumerate(num):
            lead = int(c)
            res += getLegal(N - i, lead, limit)
            if lead == 0 or lead == 1 or lead == 8 or lead == 2 or lead == 5 or lead == 6 or lead == 9:
                if lead == 2 or lead == 5 or lead == 6 or lead == 9:
                    limit = False
            else:
                break

        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.rotatedDigits(13))  # 5
    print(solution.rotatedDigits(857))  # 247
    print(solution.rotatedDigits(3))  # 1
    print(solution.rotatedDigits(31))  # 15
    print(solution.rotatedDigits(2))  # 1
    print(solution.rotatedDigits(5))  # 2
    print(solution.rotatedDigits(20))  # 9
    print(solution.rotatedDigits(22))  # 11
    print(solution.rotatedDigits(10))  # 4
    print(solution.rotatedDigits(100))  # 40
    print(solution.rotatedDigits(1000))  # 316

#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# 累加数 是一个字符串，组成它的数字可以形成累加序列。
# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
# 说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

# 示例 1：
# 输入："112358"
# 输出：true
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

# 示例 2：
# 输入："199100199"
# 输出：true
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199


# 提示：
# 1 <= num.length <= 35
# num 仅由数字（0 - 9）组成


# 进阶：你计划如何处理由过大的整数输入导致的溢出?

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        # 暴力遍历可能的前两个数切分，第二个数的终点不能超过N的2/3，也不能小于2；第一个数的终点不能超过第二个终点-1
        # 每个切分点右边字符如果是0，那么数字只能一位，就是0
        for j in range(2, (N << 1) // 3 + 1):
            b1 = 2 if num[0] == '0' else j
            for i in range(1, b1):
                if i < (j - 1) and num[i] == '0':
                    continue
                n1 = int(num[:i])
                n2 = int(num[i:j])
                e = j  # end
                while e < N:
                    n1, n2 = n2, n1 + n2
                    next = str(n2)
                    if num.find(next, e) == e:
                        e += len(next)
                        if e == N:
                            return True
                    else:
                        break

        return False


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAdditiveNumber("199001200"))  # False
    print(solution.isAdditiveNumber("0235813"))  # False
    print(solution.isAdditiveNumber("123"))  # True
    print(solution.isAdditiveNumber("112358"))  # True
    print(solution.isAdditiveNumber("199100199"))  # True

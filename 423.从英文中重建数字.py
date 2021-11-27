#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#
# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。


# 示例 1：
# 输入：s = "owoztneoer"
# 输出："012"

# 示例 2：

# 输入：s = "fviefuro"
# 输出："45"


# 提示：
# 1 <= s.length <= 10^5
# s[i] 为["e", "g", "f", "i", "h", "o", "n", "s", "r", "u", "t", "w", "v", "x", "z"] 这些字符之一
# s 保证是一个符合题目要求的字符串

# @lc code=start
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        DIGIT = [
            Counter("zero"),
            Counter("one"),
            Counter("two"),
            Counter("three"),
            Counter("four"),
            Counter("five"),
            Counter("six"),
            Counter("seven"),
            Counter("eight"),
            Counter("nine")
        ]

        cnt = Counter(s)

        # 方法1：回溯
        # TLE，重复尝试了很多场景
        # words = []

        # def backtrack(c: Counter) -> bool:
        #     for i, n in enumerate(DIGIT):
        #         c.subtract(n)
        #         words.append(i)
        #         rest = c.most_common()
        #         if rest[-1][1] >= 0:  # 有效
        #             if rest[0][1] == 0 or backtrack(c):  # 得解
        #                 return True
        #         words.pop()
        #         c += n

        # backtrack(cnt)
        # words.sort()
        # return "".join([str(w) for w in words])

        # 方法2：推理
        words = []
        resolveOrder = [(0, 'z'), (6, 'x'), (8, 'g'), (3, 'h'),
                        (2, 'w'), (7, 's'), (5, 'v'), (4, 'f'), (1, 'o'), (9, 'i')]
        for d, l in resolveOrder:
            c = cnt[l]
            words.extend([d] * c)
            a = DIGIT[d]
            for k in a.keys():
                a[k] = a[k] * c
            cnt.subtract(a)

        words.sort()
        return "".join([str(w) for w in words])

        # 方法3：矩阵求解线性方程组
        # 方法2实际上用了一些特殊的推理，并不通用，对于这类问题，通用的求解应该是构建矩阵求解线性方程组。
        # Ax = b
        # r(A) == r(A:b) == n 有唯一解
        # r(A) == r(A:b) < n 有无穷多解
        # r(A) < r(A:b) 无解

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.originalDigits("owoztneoer"))  # "012"
    print(solution.originalDigits("fviefuro"))  # "45"

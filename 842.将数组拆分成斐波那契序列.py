#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#
# 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

# 形式上，斐波那契式序列是一个非负整数列表 F，且满足：

# 0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
# F.length >= 3；
# 对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
# 另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

# 返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

# 示例 1：
# 输入："123456579"
# 输出：[123,456,579]

# 示例 2：
# 输入: "11235813"
# 输出: [1,1,2,3,5,8,13]

# 示例 3：
# 输入: "112358130"
# 输出: []
# 解释: 这项任务无法完成。

# 示例 4：
# 输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。

# 示例 5：
# 输入: "1101111"
# 输出: [110, 1, 111]
# 解释: 输出 [11,0,11,11] 也同样被接受。
 
# 提示：
# 1 <= S.length <= 200
# 字符串 S 中只含有数字。

from typing import List
# @lc code=start
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if not S:
            return []

        res = []
        L = len(S)
        LIMIT = (1 << 31) - 1

        def split(idx: int) -> bool:
            """
            在idx位置切分，是否有有效解
            """
            if idx == L:
                return len(res) >= 3

            cur = 0
            for i in range(idx, L):
                if i > idx and S[idx] == '0':
                    break
                cur = cur * 10 + ord(S[i]) - ord('0')
                if cur > LIMIT:
                    break

                if len(res) < 2 or cur == res[-1] + res[-2]:
                    res.append(cur)
                    if split(i + 1):
                        return True
                    res.pop()
                elif len(res) > 2 and cur > res[-1] + res[-2]:
                    break
            return False

        split(0)
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.splitIntoFibonacci("123456579"))
    print(solution.splitIntoFibonacci("11235813"))
    print(solution.splitIntoFibonacci("112358130"))
    print(solution.splitIntoFibonacci("0123"))
    print(solution.splitIntoFibonacci("1101111"))
    print(solution.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
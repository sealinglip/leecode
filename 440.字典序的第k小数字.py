#
# @lc app=leetcode.cn id=440 lang=python3
#
# [440] 字典序的第K小数字
#
# 给定整数 n 和 k，返回[1, n] 中字典序第 k 小的数字。


# 示例 1:
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

# 示例 2:
# 输入: n = 1, k = 1
# 输出: 1

# 提示:
# 1 <= k <= n <= 10^9


# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 找规律
        if n < 10:
            # 10以内跟字典序跟数字序一样
            return k
        # 10以上的数，其序列按字典序排列应该是
        # 以1开头的一堆，以2开头的一堆，以3开头的一堆，依次类推，最后一堆以9开头
        # 每一个子堆里，第一个数就是其本身，如果还有下一位，那么还是依次，0开头的一堆，1开头的随其后，……
        # 第一个数肯定是1
        # 最后一个数肯定是9开头

        # 思路，做dfs遍历计数，碰到了就返回
        strN = str(n)  # 数字的字符表达
        digits = len(strN)  # 数字的位数
        cnt = 0
        stack = [1]
        prefix = '1'
        while stack:
            cur = stack[-1]  # 得到当前位
            contrast = strN[:len(prefix)]
            if prefix < contrast or prefix > contrast:
                # 如果prefix < constrast，以当前前缀prefix开头的数字，只要位数不超digits，一定比n小
                # 这样的数有多少个呢？有m = digits-len(prefix)位可以填充
                # 如果prefix > constrast，以当前前缀prefix开头的数字，只要位数跟digits一样，一定比n大
                # 所以只有m = digits-len(prefix)-1位可以填充
                # 总共有11…1(共m+1位)个数
                m = digits - len(prefix)
                if prefix > contrast:
                    m -= 1
                # m 小于0，说明这数比n大，不应该在这区间里，span为0
                span = 0 if m < 0 else int('1' * (m + 1))
                if cnt + span > k:  # 说明目标数在这个区间
                    cnt += 1
                    if cnt == k:
                        return int(prefix)
                    if len(prefix) < digits:
                        stack.append(0)
                        prefix += '0'
                    else:
                        stack.pop()
                        stack[-1] += 1
                        prefix = prefix[:-2] + str(stack[-1])

                elif cnt + span == k:  # 本区间最大的数即为所求
                    return int(prefix + ('9' * m))
                else:
                    cnt += span
                    if cur < 9:
                        stack[-1] += 1
                        prefix = prefix[:-1] + str(stack[-1])
                    else:
                        while stack[-1] == 9:
                            stack.pop()
                            prefix = prefix[:-1]
                        stack[-1] += 1
                        prefix = prefix[:-1] + str(stack[-1])
            else:
                cnt += 1
                if cnt == k:
                    return int(prefix)
                if len(prefix) < digits:
                    stack.append(0)
                    prefix += '0'
                else:
                    while stack[-1] == 9:
                        stack.pop()
                        prefix = prefix[:-1]
                    stack[-1] += 1
                    prefix = prefix[:-1] + str(stack[-1])


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthNumber(1692778, 1545580))  # 867519
    print(solution.findKthNumber(100, 90))  # 9
    print(solution.findKthNumber(200, 10))  # 107
    print(solution.findKthNumber(13, 2))  # 10
    print(solution.findKthNumber(13, 12))  # 8
    print(solution.findKthNumber(1, 1))  # 1

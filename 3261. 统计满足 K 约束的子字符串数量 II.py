# 给你一个 二进制 字符串 s 和一个整数 k。
# 另给你一个二维整数数组 queries ，其中 queries[i] = [li, ri] 。
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
# 字符串中 0 的数量最多为 k。
# 字符串中 1 的数量最多为 k。
# 返回一个整数数组 answer ，其中 answer[i] 表示 s[li..ri] 中满足 k 约束 的 子字符串的数量。


# 示例 1：
# 输入：s = "0001111", k = 2, queries = [[0,6]]
# 输出：[26]
# 解释：
# 对于查询 [0, 6]， s[0..6] = "0001111" 的所有子字符串中，除 s[0..5] = "000111" 和 s[0..6] = "0001111" 外，其余子字符串都满足 k 约束。

# 示例 2：
# 输入：s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]
# 输出：[15,9,3]
# 解释：
# s 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。


# 提示：
# 1 <= s.length <= 10^5
# s[i] 是 '0' 或 '1'
# 1 <= k <= s.length
# 1 <= queries.length <= 10^5
# queries[i] == [li, ri]
# 0 <= li <= ri < s.length
# 所有查询互不相同

# Hard

from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        stat = [0, 0] # 区间计数
        prefix = [0] * (n + 1) # prefix[i]代表右边界在i之前（不含i）所有合规字符串数量
        right = [n] * n # right[i]代表以i为子字符串的左边界，最长的合规字符串的右边界（不含），即s[i:right[i]]
        i = 0
        for j in range(n):
            stat[int(s[j])] += 1
            while min(stat) > k:
                stat[int(s[i])] -= 1
                right[i] = j
                i += 1
            prefix[j + 1] = prefix[j] + j - i + 1

        res = []
        for l, r in queries:
            i = min(right[l], r + 1)
            part1 = (i - l + 1) * (i - l) // 2 # s[l:i]之间的任意字符串都合规
            part2 = prefix[r + 1] - prefix[i]
            res.append(part1 + part2)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countKConstraintSubstrings("0001111", 2, [[0,6]])) # [26]
    print(solution.countKConstraintSubstrings("010101", 1, [[0,5],[1,4],[2,3]])) # [15,9,3]

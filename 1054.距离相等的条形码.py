#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。


# 示例 1：
# 输入：barcodes = [1, 1, 1, 2, 2, 2]
# 输出：[2, 1, 2, 1, 2, 1]

# 示例 2：
# 输入：barcodes = [1, 1, 1, 1, 2, 2, 3, 3]
# 输出：[1, 3, 1, 3, 2, 1, 2, 1]


# 提示：
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000


from collections import Counter
from typing import List
# @lc code=start


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        if n < 3:
            return barcodes
        cnt = Counter(barcodes)
        kv = sorted([(k, v) for k, v in cnt.items()],
                    key=lambda i: i[1], reverse=True)
        half = (n+1) >> 1
        pivot = 0  # 记录切分点
        rest = 0
        for i, (_, v) in enumerate(kv):
            if half > v:
                half -= v
            else:
                pivot = i
                rest = v - half
                break

        i, j = 0, pivot
        l, r = kv[i][1], rest
        res = []
        for k in range(n >> 1):
            if l == 0:
                i += 1
                l = kv[i][1]
            if r == 0:
                j += 1
                r = kv[j][1]
            res.append(kv[i][0])
            res.append(kv[j][0])
            l -= 1
            r -= 1
        if n & 1:  # 奇数
            if l == 0:
                i += 1
            res.append(kv[i][0])

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.rearrangeBarcodes([1, 1, 2, 2, 3]))  # [1, 2, 1, 3, 2]
    print(solution.rearrangeBarcodes([1, 1, 2]))  # [1, 2, 1]
    print(solution.rearrangeBarcodes([1]))  # [1]
    print(solution.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))  # [2,1,2,1,2,1]
    print(solution.rearrangeBarcodes(
        [1, 1, 1, 1, 2, 2, 3, 3]))  # [1,3,1,3,2,1,2,1]

#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。
# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是(0, 1)，第二对是(2, 3)，以此类推，最后一对是(2N-2, 2N-1)。
# 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

# 示例 1:
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 我们只需要交换row[1]和row[2]的位置即可。

# 示例 2:
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。

# 说明:
# len(row) 是偶数且数值在[4, 60]范围内。
# 可以保证row 是序列 0...len(row)-1 的一个全排列。

# 提示:
# 2N == row.length
# 2 <= N <= 30
# n 是偶数
# 0 <= row[i] < 2N
# row 中所有元素均无重复

# Hard

from typing import List
# @lc code=start


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # 方法1：模拟
        # # 遍历每个偶数位置 2 * i，把它的对象安排到它右边的奇数位置 2 * i + 1
        # # 不论奇偶，x 的对象是x ^ 1
        # N = len(row)
        # res = 0
        # for i in range(0, N - 1, 2):
        #     if row[i] == row[i + 1] ^ 1:
        #         continue
        #     for j in range(i + 1, N):
        #         if row[i] == row[j] ^ 1:
        #             row[i + 1], row[j] = row[j], row[i + 1]
        #     res += 1
        # return res

        # 方法2：求连通量（并查集）
        n = len(row) >> 1
        count = n
        uf = list(range(n))

        def find(x: int) -> int:
            if x != uf[x]:
                uf[x] = find(uf[x])

            return uf[x]
        
        def union(x: int, y: int) -> None:
            nonlocal count
            x = find(x)
            y = find(y)
            if x == y:
                return
            
            uf[x] = y
            count -= 1

        for i in range(0, len(row)-1, 2):
            union(row[i] // 2, row[i+1] // 2)


        # 应该有n个连通分量（每对情路是一个连通分量），现在为了count个，每交换一次可以增加一个连通分量，所以可得知最少交换次数
        return n - count
        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwapsCouples([0, 2, 1, 3])) # 1
    print(solution.minSwapsCouples([3, 2, 0, 1])) # 0

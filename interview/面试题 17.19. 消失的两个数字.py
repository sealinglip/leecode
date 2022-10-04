# 给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

# 以任意顺序返回这两个数字均可。

# 示例 1:

# 输入: [1]
# 输出: [2, 3]
# 示例 2:

# 输入: [2, 3]
# 输出: [1, 4]
# 提示：

# nums.length <= 30000

# 来源：力扣（LeetCode）
# 链接：https: // leetcode.cn/problems/missing-two-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        N = len(nums) + 2
        totalXor = 0
        for i in range(1, N + 1):
            totalXor ^= i

        curXor = totalXor
        for num in nums:
            curXor ^= num
        # 此时 curXor应该是两个缺失数的异或 curXor = a ^ b
        # a 和 b 的最低不同位为 curXor & (-curXor)
        c = curXor & (-curXor)
        totalXor = 0
        for i in range(1, N + 1):
            if i & c:
                totalXor ^= i
        for num in nums:
            if num & c:
                totalXor ^= num
        # 此时totalXor为缺失的某个数
        return [totalXor, totalXor ^ curXor]


if __name__ == "__main__":
    solution = Solution()
    print(solution.missingTwo([1]))  # [2, 3]
    print(solution.missingTwo([2, 3]))  # [1, 4]

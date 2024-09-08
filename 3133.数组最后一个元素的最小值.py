#
# @lc app=leetcode.cn id=3133 lang=python3
#
# [3133] 数组最后一个元素的最小值
#
# 给你两个整数 n 和 x 。你需要构造一个长度为 n 的 正整数 数组 nums ，对于所有 0 <= i < n - 1 ，满足 nums[i + 1] 大于 nums[i] ，并且数组 nums 中所有元素的按位 AND 运算结果为 x 。

# 返回 nums[n - 1] 可能的 最小 值。


# 示例 1：
# 输入：n = 3, x = 4
# 输出：6
# 解释：
# 数组 nums 可以是 [4,5,6] ，最后一个元素为 6 。

# 示例 2：
# 输入：n = 2, x = 7
# 输出：15
# 解释：
# 数组 nums 可以是 [7,15] ，最后一个元素为 15 。

 
# 提示：
# 1 <= n, x <= 10^8

# @lc code=start
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # 所有元素 和 x AND 的运算结果为 x
        # 把 n-1对应二进制的各位见缝插针到x的所有为0的位上即可
        flag = 1
        m = n - 1
        res = x
        while m:
            b = m & 1 # 最右边的位
            # 从右到左找res的为0的位
            while res & flag == flag:
                flag <<= 1
            if b:
                res |= flag
            flag <<= 1
            m >>= 1
        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minEnd(3, 4)) # 6
    print(solution.minEnd(2, 7)) # 15

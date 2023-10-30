#
# @lc app=leetcode.cn id=2698 lang=python3
#
# [2698] 求一个整数的惩罚数
#
# 给你一个正整数 n ，请你返回 n 的 惩罚数 。

# n 的 惩罚数 定义为所有满足以下条件 i 的数的平方和：

# 1 <= i <= n
# i * i 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 i 。


# 示例 1：
# 输入：n = 10
# 输出：182
# 解释：总共有 3 个整数 i 满足要求：
# - 1 ，因为 1 * 1 = 1
# - 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
# - 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
# 因此，10 的惩罚数为 1 + 81 + 100 = 182

# 示例 2：
# 输入：n = 37
# 输出：1478
# 解释：总共有 4 个整数 i 满足要求：
# - 1 ，因为 1 * 1 = 1
# - 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
# - 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
# - 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。
# 因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478


# 提示：
# 1 <= n <= 1000

# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def legal(target: int, txt: str, pos: int) -> bool:
            if pos == len(txt):
                return target == 0
            total = 0
            for i in range(pos, len(txt)):
                total = total * 10 + int(txt[i])
                if total > target:
                    break
                if legal(target-total, txt, i+1):
                    return True
            return False

        return sum([i * i for i in range(1, n+1) if legal(i, str(i * i), 0)], 0)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.punishmentNumber(10))  # 182
    print(solution.punishmentNumber(37))  # 1478

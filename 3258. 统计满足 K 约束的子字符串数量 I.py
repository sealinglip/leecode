# 给你一个 二进制 字符串 s 和一个整数 k。
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：

# 字符串中 0 的数量最多为 k。
# 字符串中 1 的数量最多为 k。
# 返回一个整数，表示 s 的所有满足 k 约束 的子字符串的数量。

 
# 示例 1：
# 输入：s = "10101", k = 1
# 输出：12
# 解释：
# s 的所有子字符串中，除了 "1010"、"10101" 和 "0101" 外，其余子字符串都满足 k 约束。

# 示例 2：
# 输入：s = "1010101", k = 2
# 输出：25
# 解释：
# s 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。

# 示例 3：
# 输入：s = "11111", k = 1
# 输出：15
# 解释：
# s 的所有子字符串都满足 k 约束。

# 提示：
# 1 <= s.length <= 50
# 1 <= k <= s.length
# s[i] 是 '0' 或 '1'。
# 复习

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # 双指针，滑动窗口
        l = r = res = 0
        n = len(s)
        stat = [0] * 2
        # 移动策略：固定l，右移边界，超出限制则移动l
        while l < n:
            while r < n:
                c = int(s[r])
                stat[c] += 1
                r += 1
                if min(stat) > k:
                    break
                res += 1 # s[l:r]是合规子字符串
                # print(f"{l},{r}")
            # 超出限制，移动左边界
            while l < r:
                c = int(s[l])
                stat[c] -= 1
                l += 1
                res += max(0, r-l-1) # 以l为左边界，l+1,...,r-1为右边界（不含）的子字符串都合规
                # print(f"{l},{r}")
                if min(stat) <= k and l < r:
                    res += 1 # s[l:r]是合规字符串
                    break
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countKConstraintSubstrings("000011", 1)) # 18
    print(solution.countKConstraintSubstrings("10101", 1)) # 12
    print(solution.countKConstraintSubstrings("1010101", 2)) # 25
    print(solution.countKConstraintSubstrings("11111", 1)) # 15

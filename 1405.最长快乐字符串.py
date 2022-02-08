#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#
# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。


# 示例 1：
# 输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。

# 示例 2：
# 输入：a = 2, b = 2, c = 1
# 输出："aabbc"

# 示例 3：
# 输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。


# 提示：
# 0 <= a, b, c <= 100
# a + b + c > 0

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 设a/b/c按大小升序排为xyz，不能用完所有字母的条件为 x+y < (z-2)/2
        # 不能用完所有字母的情况，将z修正为 2(x+y)+2
        # 对于 x+y >= (z-2)/2的情况，组织答案的通用方案可以是
        # 1、如果 x+y <= z-1
        # 将z分成x+y个空，依次插入x+y对应的字符，拼接字符串
        # 2、如果 x+y > z-1
        # 将x+y分成z个空，依次插入z对应的字符，拼接字符串
        arr = [[a, 'a'], [b, 'b'], [c, 'c']]
        arr.sort()

        if arr[0][0] + arr[1][0] < (arr[2][0] - 2) / 2:
            arr[2][0] = 2 * (arr[0][0] + arr[1][0]) + 2

        if arr[0][0] + arr[1][0] <= arr[2][0] - 1:
            # z对应的字符，分成x+y+1份，其中有z-x-y-1份是double，其他是单个字符
            #
            pivot = arr[2][0] - 1 - arr[0][0] - arr[1][0]
            dz = (arr[2][1] * 2)
            split = [arr[2][1]] * \
                (arr[0][0] + arr[1][0] + 1 - pivot) + [dz] * pivot
            if arr[1][0]:
                return arr[0][1].join(split[:arr[0][0]+1]) + arr[1][1] + arr[1][1].join(split[arr[0][0]+1:])
            else:
                return arr[0][1].join(split)
        elif arr[0][0] + arr[1][0] == arr[2][0]:
            split = [arr[0][1]] * arr[0][0] + [arr[1][1]] * arr[1][0]
            return arr[2][1].join(split) + arr[2][1]
        else:
            # x+y分成z+1份，其中有x+y-z-1份是double，其他都是单个字符
            pivot = arr[0][0] + arr[1][0] - arr[2][0] - 1
            s = arr[0][1] * arr[0][0] + arr[1][1] * arr[1][0]
            pos = len(s) - (pivot << 1)
            split = [c for c in s[:pos]]
            for i in range(pivot):
                split.append(s[pos:pos + 2])
                pos += 2
            return arr[2][1].join(split)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestDiverseString(1, 0, 3))  # "ccac"
    print(solution.longestDiverseString(2, 4, 1))  # "bbaabbc"
    print(solution.longestDiverseString(1, 1, 7))  # "ccaccbcc"
    print(solution.longestDiverseString(2, 2, 1))  # "aabbc"
    print(solution.longestDiverseString(7, 1, 0))  # "aabaa"

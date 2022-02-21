#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#
# n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

# 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

# 如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。

# 就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

# 给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：

# dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
# dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
# dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
# 返回表示最终状态的字符串。


# 示例 1：
# 输入：dominoes = "RR.L"
# 输出："RR.L"
# 解释：第一张多米诺骨牌没有给第二张施加额外的力。

# 示例 2：
# 输入：dominoes = ".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."


# 提示：
# n == dominoes.length
# 1 <= n <= 105
# dominoes[i] 为 'L'、'R' 或 '.'

# @lc code=start

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        flag = [c for c in dominoes]

        def recurse(start: int, end: int):
            '''
            start: . 起始位置（包含）
            end: . 截止位置（不包含）
            '''
            # print("s:%d, e:%d" % (start, end))
            # 判断两端趋势，如果同向或一端为边界，填充成一种；如果反向，中间不变；如果相向，往中间汇拢
            if start == 0:
                if end != n and dominoes[end] == 'L':
                    for i in range(start, end):
                        flag[i] = 'L'
            elif end == n:
                if dominoes[start - 1] == 'R':
                    for i in range(start, end):
                        flag[i] = 'R'
            elif dominoes[start - 1] == dominoes[end]:
                for i in range(start, end):
                    flag[i] = dominoes[start - 1]
            elif dominoes[start - 1] == 'R' and dominoes[end] == 'L':
                for i in range((end-start) >> 1):
                    flag[start+i] = 'R'
                    flag[end-i-1] = 'L'

        if '.' in dominoes:
            e = -1
            while (s := dominoes.find('.', e + 1)) != -1:
                e = s
                while e < n - 1 and dominoes[e+1] == '.':
                    e += 1
                # dominoes[s:e+1] 都是'.'
                recurse(s, e+1)

        return "".join(flag)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.pushDominoes("RR.L"))  # "RR.L"
    print(solution.pushDominoes(".L.R...LR..L.."))  # "LL.RR.LLRRLL.."

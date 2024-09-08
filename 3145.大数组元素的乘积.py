# 一个非负整数 x 的 强数组 指的是满足元素为 2 的幂且元素总和为 x 的最短有序数组。下表说明了如何确定 强数组 的示例。可以证明，x 对应的强数组是独一无二的。

# 数字	二进制表示	强数组
# 1	00001	[1]
# 8	01000	[8]
# 10	01010	[2, 8]
# 13	01101	[1, 4, 8]
# 23	10111	[1, 2, 4, 16]
 

# 我们将每一个升序的正整数 i （即1，2，3等等）的 强数组 连接得到数组 big_nums ，big_nums 开始部分为 [1, 2, 1, 2, 4, 1, 4, 2, 4, 1, 2, 4, 8, ...] 。
# 给你一个二维整数数组 queries ，其中 queries[i] = [fromi, toi, modi] ，你需要计算 (big_nums[fromi] * big_nums[fromi + 1] * ... * big_nums[toi]) % modi 。
# 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。


# 示例 1：
# 输入：queries = [[1,3,7]]
# 输出：[4]
# 解释：
# 只有一个查询。
# big_nums[1..3] = [2,1,2] 。它们的乘积为 4。结果为 4 % 7 = 4。

# 示例 2：
# 输入：queries = [[2,5,3],[7,7,4]]
# 输出：[2,2]
# 解释：
# 有两个查询。
# 第一个查询：big_nums[2..5] = [1,2,4,1] 。它们的乘积为 8 。结果为  8 % 3 = 2。
# 第二个查询：big_nums[7] = 2 。结果为 2 % 4 = 2。
 

# 提示：
# 1 <= queries.length <= 500
# queries[i].length == 3
# 0 <= queries[i][0] <= queries[i][1] <= 10^15
# 1 <= queries[i][2] <= 10^5

# Hard

from typing import List

# maxInfo 70368744177664 (1 << 46), 1618481116086273
# MAX_NUM = 1_000_000_000_000_000

num2exp, exp2num = {}, {}
for _index in range(47):
    _num = 1 << _index
    num2exp[_num] = _index
    exp2num[_index] = _num

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        
        def check(targetLength: int) -> int:
            curNum = curLen = curCnt = curMul = curRes = 0
            for curExp in range(targetLength.bit_length() - 1, 0, -1):
                # nextLen = curLen + (curExp << (curExp - 1)) + 1 + (curCnt << curExp)
                nextLen = curLen + (curExp + curCnt + curCnt << curExp - 1) + 1
                if nextLen <= targetLength:
                    curLen = nextLen
                    curCnt += 1
                    curNum |= exp2num[curExp]
                    curRes += ((curExp - 1) * curExp >> 1 << (curExp - 1)) + curExp + (curMul << curExp)
                    curMul += curExp
            nextLen = curLen + 1 + curCnt
            if nextLen <= targetLength:
                curLen = nextLen
                curNum |= 1
                curRes += curMul
            curNum += 1
            while curLen < targetLength:
                low = curNum & -curNum
                curRes += num2exp[low] # 这里如果使用 low.bit_length() 可以彻底不预计算任何数字
                curNum ^= low
                curLen += 1
            return curRes

        return [pow(2, check(tail + 1) - check(head), mod) for head, tail, mod in queries]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findProductsOfElements([[1,3,7]])) # [4]
    print(solution.findProductsOfElements([[2,5,3],[7,7,4]])) # [2,2]

# 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。 
# 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。

# 示例 1：
# 输入：cards = [1,2,8,9], cnt = 3
# 输出：18
# 解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。

# 示例 2：
# 输入：cards = [3,3,1], cnt = 1
# 输出：0
# 解释：不存在获取有效得分的卡牌方案。

# 提示：
# 1 <= cnt <= cards.length <= 10^5
# 1 <= cards[i] <= 1000

from typing import List

class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        res = sum(cards[:cnt])
        if res & 1 == 0:
            return res
        else:
            # 要么从cards[cnt:]中找出最大的奇数和cards[:cnt]中最小的偶数替换
            # 要么从cards[cnt:]中找出最大的偶数和cards[:cnt]中最小的奇数替换
            maOdd = maEven = -1
            for c in cards[cnt:]:
                if c & 1 == 0:
                    if c > maEven:
                        maEven = c
                elif c > maOdd:
                    maOdd = c

            miOdd = miEven = 1001
            for c in cards[:cnt]:
                if c & 1 == 0:
                    if c < miEven:
                        miEven = c
                elif c < miOdd:
                    miOdd = c

            delta = 1001
            if maOdd != -1 and miEven != 1001:
                delta = min(delta, miEven - maOdd)
            if maEven != -1 and miOdd != 1001:
                delta = min(delta, miOdd - maEven)
            
            return 0 if delta == 1001 else (res - delta)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxmiumScore([1,2,8,9], 3)) # 18
    print(solution.maxmiumScore([3,3,1], 1)) # 0

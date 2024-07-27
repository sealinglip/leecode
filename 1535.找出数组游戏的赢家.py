#
# @lc app=leetcode.cn id=1535 lang=python3
#
# [1535] 找出数组游戏的赢家
#
# 给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。

# 每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。

# 返回赢得比赛的整数。

# 题目数据 保证 游戏存在赢家。


# 示例 1：
# 输入：arr = [2,1,3,5,4,6,7], k = 2
# 输出：5
# 解释：一起看一下本场游戏每回合的情况：
# 因此将进行 4 回合比赛，其中 5 是赢家，因为它连胜 2 回合。

# 示例 2：
# 输入：arr = [3,2,1], k = 10
# 输出：3
# 解释：3 将会在前 10 个回合中连续获胜。

# 示例 3：
# 输入：arr = [1,9,8,2,3,7,6,4,5], k = 7
# 输出：9

# 示例 4：
# 输入：arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
# 输出：99
 

# 提示：
# 2 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^6
# arr 所含的整数 各不相同 。
# 1 <= k <= 10^9


from typing import List
# @lc code=start
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 不用管被扔到尾巴上的loser，它们只能凑人头
        n = len(arr)
        winstreak, winner = 0, arr[0]
        for i in range(1, n):
            if winner > arr[i]:
                winstreak += 1
            else:
                winstreak, winner = 1, arr[i]
            if winstreak >= k:
                break
        return winner

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.getWinner([2,1,3,5,4,6,7], 2)) # 5
    print(solution.getWinner([3,2,1], 10)) # 3
    print(solution.getWinner([1,9,8,2,3,7,6,4,5], 7)) # 9
    print(solution.getWinner([1,11,22,33,44,55,66,77,88,99], 1000000000)) # 99
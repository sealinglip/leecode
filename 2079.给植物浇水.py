#
# @lc app=leetcode.cn id=2079 lang=python3
#
# [2079] 给植物浇水
#
# 你打算用一个水罐给花园里的 n 株植物浇水。植物排成一行，从左到右进行标记，编号从 0 到 n - 1 。其中，第 i 株植物的位置是 x = i 。x = -1 处有一条河，你可以在那里重新灌满你的水罐。

# 每一株植物都需要浇特定量的水。你将会按下面描述的方式完成浇水：

# 按从左到右的顺序给植物浇水。
# 在给当前植物浇完水之后，如果你没有足够的水 完全 浇灌下一株植物，那么你就需要返回河边重新装满水罐。
# 你 不能 提前重新灌满水罐。
# 最初，你在河边（也就是，x = -1），在 x 轴上每移动 一个单位 都需要 一步 。

# 给你一个下标从 0 开始的整数数组 plants ，数组由 n 个整数组成。其中，plants[i] 为第 i 株植物需要的水量。另有一个整数 capacity 表示水罐的容量，返回浇灌所有植物需要的 步数 。


# 示例 1：
# 输入：plants = [2,2,3,3], capacity = 5
# 输出：14
# 解释：从河边开始，此时水罐是装满的：
# - 走到植物 0 (1 步) ，浇水。水罐中还有 3 单位的水。
# - 走到植物 1 (1 步) ，浇水。水罐中还有 1 单位的水。
# - 由于不能完全浇灌植物 2 ，回到河边取水 (2 步)。
# - 走到植物 2 (3 步) ，浇水。水罐中还有 2 单位的水。
# - 由于不能完全浇灌植物 3 ，回到河边取水 (3 步)。
# - 走到植物 3 (4 步) ，浇水。
# 需要的步数是 = 1 + 1 + 2 + 3 + 3 + 4 = 14 。

# 示例 2：
# 输入：plants = [1,1,1,4,2,3], capacity = 4
# 输出：30
# 解释：从河边开始，此时水罐是装满的：
# - 走到植物 0，1，2 (3 步) ，浇水。回到河边取水 (3 步)。
# - 走到植物 3 (4 步) ，浇水。回到河边取水 (4 步)。
# - 走到植物 4 (5 步) ，浇水。回到河边取水 (5 步)。
# - 走到植物 5 (6 步) ，浇水。
# 需要的步数是 = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30 。

# 示例 3：
# 输入：plants = [7,7,7,7,7,7,7], capacity = 8
# 输出：49
# 解释：每次浇水都需要重新灌满水罐。
# 需要的步数是 = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49 。
 

# 提示：
# n == plants.length
# 1 <= n <= 1000
# 1 <= plants[i] <= 10^6
# max(plants[i]) <= capacity <= 10^9

from typing import List
# @lc code=start
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # 模拟
        n = len(plants)
        
        cur = 0 # 待浇水的植物位置
        steps = 0 # 步数
        pos = -1 # 人位置
        rest = capacity # 水
        while cur < n:
            if rest >= plants[cur]:
                # 水够浇
                rest -= plants[cur]
                steps += cur - pos
                pos = cur
                cur += 1
            else:
                # 回去取水
                steps += pos + 1
                pos = -1
                rest = capacity

        return steps
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.wateringPlants([2,2,3,3], 5)) # 14
    print(solution.wateringPlants([1,1,1,4,2,3], 4)) # 30
    print(solution.wateringPlants([7,7,7,7,7,7,7], 8)) # 49
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。
# 由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

# 示例：
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]

# 提示：
# 0 < len(land) <= 1000
# 0 < len(land[i]) <= 1000


from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        DIR = [-1, -1, 0, -1, 1, 1, 0, 1, -1]
        m, n = len(land), len(land[0])

        def dfs(x: int, y: int) -> int:
            land[x][y] = -1
            res = 1
            for i in range(8):
                nx, ny = x + DIR[i], y + DIR[i+1]
                if 0 <= nx < m and 0 <= ny < n and land[nx][ny] == 0:
                    res += dfs(nx, ny)

            return res

        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    res.append(dfs(i, j))

        return sorted(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]))  # [1,2,4]

# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

# 示例：
# 输入： arr = [1, 3, 5, 7, 2, 4, 6, 8], k = 4
# 输出： [1, 2, 3, 4]

# 提示：
# 0 <= len(arr) <= 100000
# 0 <= k <= min(100000, len(arr))

from typing import List
import heapq


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        res = [-x for x in arr[:k]]
        heapq.heapify(res)  # 转成堆
        for num in arr[k:]:
            if num < -res[0]:
                heapq.heappop(res)
                heapq.heappush(res, -num)
        res = [-x for x in res]
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestK([1, 3, 5, 7, 2, 4, 6, 8], 4))

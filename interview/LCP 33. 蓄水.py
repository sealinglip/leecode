# 给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：

# 升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
# 蓄水：将全部水桶接满水，倒入各自对应的水缸
# 每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

# 注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。

# 示例 1：
# 输入：bucket = [1,3], vat = [6,8]
# 输出：4
# 解释：
# 第 1 次操作升级 bucket[0]；
# 第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。

# 示例 2：
# 输入：bucket = [9,0,1], vat = [0,2,2]
# 输出：3
# 解释：
# 第 1 次操作均选择升级 bucket[1]
# 第 2~3 次操作选择蓄水，即可完成蓄水要求。

# 提示：
# 1 <= bucket.length == vat.length <= 100
# 0 <= bucket[i], vat[i] <= 10^4

# 复习
import heapq
from math import inf
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        pq = []  # 优先队列
        cnt = 0  # 记录扩容次数
        for i in range(n):
            b, v = bucket[i], vat[i]
            if b == 0 and v:
                cnt += 1
                bucket[i] = b = 1
            if v > 0:
                heapq.heappush(pq, [-((v + b - 1) // b), i])

        if not pq:
            return 0  # vat全是0

        res = inf
        while cnt < res:
            v, i = heapq.heappop(pq)
            v = -v
            res = min(res, cnt + v)
            if v == 1:  # 只用蓄水一次，不可能通过扩容压缩次数了
                break
            t = (vat[i] + v - 2) // (v - 1)  # 要将蓄水次数压缩一次，对应水桶至少需要达到的容量
            cnt += t - bucket[i]
            bucket[i] = t
            heapq.heappush(pq, [-((vat[i] + t - 1) // t), i])

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.storeWater([1, 3], [6, 8]))  # 4
    print(solution.storeWater([9, 0, 1], [0, 2, 2]))  # 3

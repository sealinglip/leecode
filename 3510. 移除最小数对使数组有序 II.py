# 给你一个数组 nums，你可以执行以下操作任意次数：
# 选择 相邻 元素对中 和最小 的一对。如果存在多个这样的对，选择最左边的一个。
# 用它们的和替换这对元素。

# 返回将数组变为 非递减 所需的 最小操作次数 。

# 如果一个数组中每个元素都大于或等于它前一个元素（如果存在的话），则称该数组为非递减。
 

# 示例 1：
# 输入： nums = [5,2,3,1]
# 输出： 2
# 解释：
# 元素对 (3,1) 的和最小，为 4。替换后 nums = [5,2,4]。
# 元素对 (2,4) 的和为 6。替换后 nums = [5,6]。
# 数组 nums 在两次操作后变为非递减。

# 示例 2：
# 输入： nums = [1,2,2]
# 输出： 0
# 解释：
# 数组 nums 已经是非递减的。


# 提示：
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

from heapq import heappop, heappush
from typing import List

class Node:
    def __init__(self, val: int, idx: int):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        class PQItem:
            def __init__(self, first: Node, second: Node, pairSum: int):
                self.first = first
                self.second = second
                self.pairSum = pairSum

            def __lt__(self, other):
                if self.pairSum == other.pairSum:
                    return self.first.idx < other.first.idx
                return self.pairSum < other.pairSum
        
        pq = [] # 优先队列
        head = Node(nums[0], 0)
        descreaseCnt = 0
        merged = [False] * len(nums)

        # 构建双向链表、优先队列，记录非递增数量
        cur = head
        for i in range(1, len(nums)):
            node = Node(nums[i], i)
            cur.next = node
            node.prev = cur
            heappush(pq, PQItem(cur, node, cur.val + node.val))

            if nums[i - 1] > nums[i]:
                descreaseCnt += 1

            cur = node

        count = 0
        while descreaseCnt > 0:
            item = heappop(pq)
            fi, se, ps = item.first, item.second, item.pairSum

            if merged[fi.idx] or merged[se.idx] or fi.val + se.val != ps:
                # 已经失效的数据
                continue

            count += 1

            if fi.val > se.val:
                descreaseCnt -= 1

            prevNode = fi.prev
            nextNode = se.next
            fi.next = nextNode
            if nextNode:
                nextNode.prev = fi

            if prevNode:
                if prevNode.val > fi.val and prevNode.val <= ps:
                    descreaseCnt -= 1
                elif prevNode.val <= fi.val and prevNode.val > ps:
                    descreaseCnt += 1
                
                heappush(pq, PQItem(prevNode, fi, prevNode.val + ps))

            if nextNode:
                if se.val > nextNode.val and ps <= nextNode.val:
                    descreaseCnt -= 1
                elif se.val <= nextNode.val and ps > nextNode.val:
                    descreaseCnt += 1
                
                heappush(pq, PQItem(fi, nextNode, ps + nextNode.val))

            fi.val = ps
            merged[se.idx] = True

        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumPairRemoval([5,2,3,1])) # 2
    print(solution.minimumPairRemoval([1,2,2])) # 0

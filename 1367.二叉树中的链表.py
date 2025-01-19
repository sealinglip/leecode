#
# @lc app=leetcode.cn id=1367 lang=python3
#
# [1367] 二叉树中的链表
#
# 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。

# 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。

# 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。


# 示例 1：
# 输入：head = [4,2,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
# 输出：true
# 解释：树中蓝色的节点构成了与链表对应的子路径。

# 示例 2：
# 输入：head = [1,4,2,6], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
# 输出：true

# 示例 3：
# 输入：head = [1,4,2,6,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
# 输出：false
# 解释：二叉树中不存在一一对应链表的路径。
 

# 提示：
# 二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
# 链表包含的节点数目在 1 到 100 之间。
# 二叉树包含的节点数目在 1 到 2500 之间。

# 复习
# 应该可以用KMP做优化

from listnode import ListNode
from treenode import TreeNode
from typing import Optional, List

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # 因为链表不大，直接转成列表
        l = []
        while head:
            l.append(head.val)
            head = head.next
        n = len(l)

        # 构造KMP的next数组
        def buildNext(arr: List[int]) -> List[int]:
            nxt = [0] * len(arr)
            j = 0
            for i in range(1, len(arr)):
                while j > 0 and arr[i] != arr[j]:
                    j = nxt[j-1]
                if arr[i] == arr[j]:
                    j += 1
                nxt[i] = j
            return nxt
        
        nxt = buildNext(l)

        def search(treeNode: TreeNode, i: int) -> bool:
            if treeNode is None:
                return False
            
            while i > 0 and treeNode.val != l[i]:
                i = nxt[i-1]
            if treeNode.val == l[i]:
                i += 1

            if i >= n:
                return True
            
            return search(treeNode.left, i) or search(treeNode.right, i)
        
        return search(root, 0)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubPath(ListNode.convert_list([2,2,1]), TreeNode.createBFSTree([2,None,2,None,2,None,1]))) # True
    print(solution.isSubPath(ListNode.convert_list([1,10]), TreeNode.createBFSTree([1,None,1,10,1,9]))) # True
    print(solution.isSubPath(ListNode.convert_list([4,2]), TreeNode.createBFSTree([4,4,4,1,None,None,None,2]))) # False
    print(solution.isSubPath(ListNode.convert_list([4,2,8]), TreeNode.createBFSTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]))) # True
    print(solution.isSubPath(ListNode.convert_list([1,4,2,6]), TreeNode.createBFSTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]))) # True
    print(solution.isSubPath(ListNode.convert_list([1,4,2,6,8]), TreeNode.createBFSTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]))) # False


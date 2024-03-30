#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#
# 给出一个满足下述规则的二叉树：

# root.val == 0
# 如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
# 如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
# 现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。

# 请你先还原二叉树，然后实现 FindElements 类：

# FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
# bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。
 

# 示例 1：
# 输入：
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# 输出：
# [null,false,true]
# 解释：
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 

# 示例 2：
# 输入：
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# 输出：
# [null,true,true,false]
# 解释：
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False

# 示例 3：
# 输入：
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# 输出：
# [null,true,false,false,true]
# 解释：
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True
 

# 提示：
# TreeNode.val == -1
# 二叉树的高度不超过 20
# 节点的总数在 [1, 10^4] 之间
# 调用 find() 的总次数在 [1, 10^4] 之间
# 0 <= target <= 10^6


from treenode import TreeNode
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self._root = root
        self.__correct(root)

    def __correct(self, node: TreeNode):
        if node.left:
            node.left.val = (node.val << 1) + 1
            self.__correct(node.left)
        if node.right:
            node.right.val = (node.val << 1) + 2
            self.__correct(node.right)

    def find(self, target: int) -> bool:
        # 将target转换为查找路径
        path = []
        while target:
            path.append(target & 1) # 1 代表左, 0 代表右
            target = (target - 1) >> 1
        # 翻转得到从根节点出发找该值的路径
        path.reverse()
        node = self._root
        for p in path:
            if not node:
                return False
            elif p:
                node = node.left
            else:
                node = node.right
        return node is not None
        

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

if __name__ == "__main__":
    findElements = FindElements(TreeNode.createBFSTree([-1, None, -1]))
    print(findElements.find(1)) # False
    print(findElements.find(2)) # True

    findElements = FindElements(TreeNode.createBFSTree([-1,-1,-1,-1,-1]))
    print(findElements.find(1)) # True
    print(findElements.find(3)) # True
    print(findElements.find(5)) # False
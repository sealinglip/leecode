#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#
# 你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
# 如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
# 文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
# 例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。


# 示例 1：
# 输入：folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
# 输出：["/a", "/c/d", "/c/f"]
# 解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

# 示例 2：
# 输入：folder = ["/a", "/a/b/c", "/a/b/d"]
# 输出：["/a"]
# 解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。

# 示例 3：
# 输入: folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]
# 输出: ["/a/b/c", "/a/b/ca", "/a/b/d"]


# 提示：
# 1 <= folder.length <= 4 * 10^4
# 2 <= folder[i].length <= 100
# folder[i] 只包含小写字母和 '/'
# folder[i] 总是以字符 '/' 起始
# 每个文件夹名都是 唯一 的


from typing import List
# @lc code=start


class Trie:
    def __init__(self, name=None, end=False) -> None:
        self._name = name
        self._end = end
        self._children = {}

    def getChild(self, name) -> 'Trie':
        return self._children.get(name, None)

    def findOrCreatePath(self, path) -> 'Trie':
        parts = path.split('/')
        curObj = self
        n = len(parts)
        for i, part in enumerate(parts):
            child = curObj.getChild(part)
            if child is None:
                child = Trie(part, i == n - 1)
                curObj._children[part] = child
            curObj = child
            if curObj._end:
                break

        if not curObj._end:
            curObj.clearChildren()
            curObj._end = True
        return curObj

    def clearChildren(self) -> None:
        self._children.clear()

    def dumpPath(self, folder: List[str]) -> None:
        self._dumpPath('', folder)

    def _dumpPath(self, prefix: str, folder: List[str]) -> None:
        prefix += '/' + self._name if self._name else ''
        if self._end:
            folder.append(prefix)
        else:
            for v in self._children.values():
                v._dumpPath(prefix, folder)


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for f in folder:
            root.findOrCreatePath(f)

        res = []
        root.dumpPath(res)
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # ["/a","/c/d","/c/f"]
    print(solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
    print(solution.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))  # ["/a"]
    # ["/a/b/c","/a/b/ca","/a/b/d"]
    print(solution.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))

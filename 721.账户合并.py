#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称(name)，其余元素是 emails 表示该账户的邮箱地址。
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

# 示例 1：
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#     ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案[['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
#                    ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。

# 提示：
# accounts的长度将在[1，1000]的范围内。
# accounts[i]的长度将在[1，10]的范围内。
# accounts[i][j]的长度将在[1，30]的范围内。

from typing import List
# @lc code=start


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rootMap = {}

    def find(self, email: str):
        parent = self.parent[email]
        if parent == email:
            return parent
        else:
            root = self.parent[parent]
            if root != parent:
                while self.parent[root] != root:
                    root = self.parent[root]

                # 压缩路径
                while email != root:
                    original_father = self.parent[email]
                    self.parent[email] = root
                    email = original_father
            return root

    def merge(self, e1: str, e2: str) -> str:
        r1, r2 = self.find(e1), self.find(e2)
        if r1 != r2:
            self.parent[r1] = r2
            v = self.rootMap.pop(r1)
            self.rootMap[r2][1].extend(v[1])
        return r2

    def add(self, account) -> str:
        name = account[0]
        root = None
        for i in range(1, len(account)):
            if account[i] not in self.parent:
                if root is None:
                    self.parent[account[i]] = account[i]
                    self.rootMap[account[i]] = (name, [account[i]])
                    root = account[i]
                else:
                    self.parent[account[i]] = root
                    self.rootMap[root][1].append(account[i])
            else:
                if root is None:
                    root = self.find(account[i])
                else:
                    root = self.merge(account[i], root)
        return root


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return []

        # 并查集
        uf = UnionFind()
        for account in accounts:
            uf.add(account)

        # 输出结果
        res = []
        for key in uf.rootMap:
            value = uf.rootMap[key]
            value[1].sort()
            res.append([value[0], *value[1]])
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], [
          "John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
    print(solution.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], [
          "John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))

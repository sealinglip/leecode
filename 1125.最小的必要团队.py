#
# @lc app=leetcode.cn id=1125 lang=python3
#
# [1125] 最小的必要团队
#
# 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。

# 所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：

# 例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
# 请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。


# 示例 1：
# 输入：req_skills = ["java", "nodejs", "reactjs"], people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
# 输出：[0, 2]

# 示例 2：
# 输入：req_skills = ["algorithms", "math", "java", "reactjs", "csharp", "aws"], people = [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]
# 输出：[1, 2]


# 提示：
# 1 <= req_skills.length <= 16
# 1 <= req_skills[i].length <= 16
# req_skills[i] 由小写英文字母组成
# req_skills 中的所有字符串 互不相同
# 1 <= people.length <= 60
# 0 <= people[i].length <= 16
# 1 <= people[i][j].length <= 16
# people[i][j] 由小写英文字母组成
# people[i] 中的所有字符串 互不相同
# people[i] 中的每个技能是 req_skills 中的技能
# 题目数据保证「必要团队」一定存在

# Hard
# 复习

from typing import List
# @lc code=start


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 集合覆盖问题（Set Covering Problem，简称 SCP）
        n, m = len(req_skills), len(people)  # 技能数、人数
        skill_idx = {v: i for i, v in enumerate(req_skills)}  # 技能映射到位序号
        # 记dp[i]为满足技能集合为i的最小人数，dp[0] = 0，其他dp初始为最大值
        dp = [m] * (1 << n)
        dp[0] = 0
        prev_skill = [0] * (1 << n)  # 追溯最优解用
        prev_people = [0] * (1 << n)  # 同上

        for i, p in enumerate(people):
            cur_skill = 0  # 记录当前人的技能
            for s in p:
                cur_skill |= 1 << skill_idx[s]

            for prev in range(1 << n):
                comb = prev | cur_skill
                if dp[comb] > dp[prev] + 1:
                    dp[comb] = dp[prev] + 1
                    prev_skill[comb] = prev
                    prev_people[comb] = i

        res = []
        i = (1 << n) - 1
        while i > 0:
            res.append(prev_people[i])
            i = prev_skill[i]
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestSufficientTeam(["java", "nodejs", "reactjs"], [
          ["java"], ["nodejs"], ["nodejs", "reactjs"]]))  # [0, 2]
    print(solution.smallestSufficientTeam(["algorithms", "math", "java", "reactjs", "csharp", "aws"], [["algorithms", "math", "java"], [
          "algorithms", "math", "reactjs"], ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]))  # [1, 2]

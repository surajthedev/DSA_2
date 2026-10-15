# In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

# Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

# For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
# Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

# It is guaranteed an answer exists.



# Example 1:

# Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
# Example 2:

# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]


# Constraints:

# 1 <= req_skills.length <= 16
# 1 <= req_skills[i].length <= 16
# req_skills[i] consists of lowercase English letters.
# All the strings of req_skills are unique.
# 1 <= people.length <= 60
# 0 <= people[i].length <= 16
# 1 <= people[i][j].length <= 16
# people[i][j] consists of lowercase English letters.
# All the strings of people[i] are unique.
# Every skill in people[i] is a skill in req_skills.
# It is guaranteed a sufficient team exists.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ### Brute Force — Backtracking

python
```
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_map = {skill: i for i, skill in enumerate(req_skills)}
        target = (1 << n) - 1

        masks = []
        for person in people:
            mask = 0
            for skill in person:
                mask |= 1 << skill_map[skill]
            masks.append(mask)

        ans = list(range(len(people) + 1))

        def dfs(i, mask, team):
            nonlocal ans

            if mask == target:
                if len(team) < len(ans):
                    ans = team[:]
                return

            if i == len(people) or len(team) >= len(ans):
                return

            dfs(i + 1, mask, team)

            new_mask = mask | masks[i]
            if new_mask != mask:
                team.append(i)
                dfs(i + 1, new_mask, team)
                team.pop()

        dfs(0, 0, [])
        return ans
```

### Optimal — Bitmask DP

python
```
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_map = {skill: i for i, skill in enumerate(req_skills)}
        target = (1 << len(req_skills)) - 1

        dp = {0: []}

        for i, person in enumerate(people):
            person_mask = 0

            for skill in person:
                person_mask |= 1 << skill_map[skill]

            for mask, team in list(dp.items()):
                new_mask = mask | person_mask

                if new_mask == mask:
                    continue

                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]

        return dp[target]
```

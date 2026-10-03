class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans: list[list[str]] = []
        n = len(strs)
        count: dict[tuple[int], list[str]] = {}

        for i in range(n):
            temp: list[int] = [0] * 26
            for j in range(len(strs[i])):
                temp[ord(strs[i][j]) - ord('a')] += 1

            key: tuple[int] = tuple(temp)
            if key not in count:
                count[key] = []
            count[key].append(strs[i])

        for key in count:
            ans.append(count[key])
        return ans
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        m = sorted(c, key=c.get, reverse=True)


        return [m[n] for n in range(k)]
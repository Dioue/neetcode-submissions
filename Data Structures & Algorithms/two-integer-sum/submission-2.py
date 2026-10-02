class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hmap = {nums[0]: 0}

        for i in range(1, n):
            c = target - nums[i]
            if c in hmap:
                return [hmap[c], i]
                
            if nums[i] not in hmap:
                hmap[nums[i]] = i
            
        return [0, 0]
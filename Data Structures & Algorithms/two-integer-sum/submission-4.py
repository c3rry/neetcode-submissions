class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in hmp:
                return [hmp[complement], index]
            hmp[num] = index
        return []
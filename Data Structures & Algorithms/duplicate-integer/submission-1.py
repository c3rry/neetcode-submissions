class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        num_s = nums

        for i in range(1, len(num_s)):
            if num_s[i] == num_s[i - 1]:
                return True
                break
        return False
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 0

        max_list = []
        for i in range(k):
            max_key = max(freq, key = freq.get)
            freq.pop(max_key, None)
            max_list.append(max_key)

        return max_list

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []
        for num, Frequency in sorted(
            freq.items(),
            key = lambda x : x[1],
            reverse = True
        ):
            result.append(num)
            if len(result) == k:
                break

        return result;
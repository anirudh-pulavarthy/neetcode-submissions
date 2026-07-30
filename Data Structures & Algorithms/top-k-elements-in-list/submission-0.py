from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums: counts[n] += 1

        most_freq = [(i, count) for i, count in counts.items()]
        most_freq = sorted(most_freq, key=lambda a: a[1], reverse = True)
        most_freq = list(map(lambda x:x[0], most_freq))
        return most_freq[:k]
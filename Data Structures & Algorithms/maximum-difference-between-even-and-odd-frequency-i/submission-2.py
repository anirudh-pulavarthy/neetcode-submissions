from operator import itemgetter

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        even = []
        odd = []
        for char, count in counts.items():
            if count % 2 == 0:
                even.append((char, count))
            else:
                odd.append((char, count))
        
        even = sorted(even, key=itemgetter(1))
        odd = sorted(odd, key=itemgetter(1))

        return (odd[-1][1] - even[0][1])
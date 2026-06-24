class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        counts = Counter(nums)
        for num,count in counts.items():
            buckets[count - 1 ].append(num)
        output = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(output) == k:
                break;
            if buckets[i]:
                output.extend(buckets[i])
        return output


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for num,count in counts.items():
            buckets[count].append(num)
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(output) == k:
                break;
            for n in buckets[i]:
                output.append(n)        
        return output


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [set() for _ in range(len(nums))]
        count = {}
        for num in nums:
            currentC = count.get(num, -1)
            if currentC != -1:
                buckets[currentC].remove(num)
            count[num] = currentC + 1
            buckets[currentC + 1].add(num)
        c = k
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            if c == 0:
                break;
            if buckets[i]:
                output.extend(list(buckets[i]))
                c -= 1
        return output


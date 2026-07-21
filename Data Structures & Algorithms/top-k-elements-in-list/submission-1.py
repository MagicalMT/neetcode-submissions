class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        result = []
        for i in nums:
            temp[i] += 1
        sortednum = sorted(temp.items(), key=lambda x: x[1], reverse = True)
        for j in range(k):
            result.append(sortednum[j][0])
        return result
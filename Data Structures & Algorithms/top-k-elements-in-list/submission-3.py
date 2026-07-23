class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        listNum = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for n, c in count.items():
            listNum[c].append(n)
        
        for i in range(len(nums), 0, -1):
            for num in listNum[i]:
                res.append(num)
                if len(res) == k:
                    return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNum = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if(number in dictNum):
                return [dictNum[number], i]
            dictNum[nums[i]] = i
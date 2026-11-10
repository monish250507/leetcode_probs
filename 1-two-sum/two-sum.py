class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap ={}
        for i , num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return (hashmap[difference], i)
            hashmap[num]=i
        return 
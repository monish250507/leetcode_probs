class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        curmin , curmax=1,1
        for num in nums:
            temp = curmax*num
            curmax = max(temp , num* curmin , num)
            curmin=min(temp , num*curmin , num)
            result = max(result , curmax)
        return result
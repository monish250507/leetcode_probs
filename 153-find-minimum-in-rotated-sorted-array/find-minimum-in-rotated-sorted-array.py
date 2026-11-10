class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        l , r = 0 , len(nums)-1
        while l<=r:
            m=(l+r)//2
            if (nums[l]<nums[r]):
                result = min(result , nums[l])
                break
            result =min(result , nums[m])
            if (nums[m]>=nums[l]):
                l=m+1
            else:
                r=m-1
        return result
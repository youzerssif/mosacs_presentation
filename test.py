from typing import List





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for item in range(len(nums)-1):
            print(nums[item] , nums[item+1], nums.index(nums[item+1]))
            if nums[item] + nums[item+1]==target:
                nexi = nums.index(nums[item])+1
                return [nums.index(nums[item]), nums.index(nums[item+1],nexi)]


obj = Solution()
print(obj.twoSum([3,2,3],6))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def add(a,b):
            c=a+b
            return c
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum=add(nums[i],nums[j])
                if sum==target:
                    return i,j
                
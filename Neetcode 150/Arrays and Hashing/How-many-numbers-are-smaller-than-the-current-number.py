class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedarray = sorted(nums)
        for i in range(len(sortedarray)):
            if nums[i] == min(sortedarray):
                nums[i] = 0
            else:
                nums[i] = sortedarray.index(nums[i])
        return nums
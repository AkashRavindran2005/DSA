class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n1 = 0
        maxnum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                n1 += 1
                maxnum = max(maxnum, n1)
            else:
                n1 = 0
        return maxnum

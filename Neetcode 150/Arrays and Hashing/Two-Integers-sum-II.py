class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            if target - numbers[i] in d and target-numbers[i] != numbers[i]:
                return [d[target-numbers[i]], i+1]
            d[numbers[i]] = i + 1

#Optimal Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            if sum > target:
                right -= 1
            if sum == target:
                return [left+1, right+1]
                

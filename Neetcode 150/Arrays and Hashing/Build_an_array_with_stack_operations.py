class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        num = 0
        for i in range(1, n+1):
            if num == len(target):
                break
            ops.append("Push")
            if i == target[num]:
                num += 1
            else:
                ops.append("Pop")
        return ops

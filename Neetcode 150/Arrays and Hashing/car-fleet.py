class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        fleets = 1
        prevtime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currcar = pair[i]
            currtime = (target - currcar[0]) / currcar[1]
            if currtime > prevtime:
                fleets += 1
                prevtime = currtime
        return fleets
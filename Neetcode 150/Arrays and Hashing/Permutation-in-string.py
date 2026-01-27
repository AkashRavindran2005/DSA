class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        window = len(s1)
        matched = 0
        for i in range(len(s2)):
            if counter[s2[i]] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    matched += 1
            if i >= window and s2[i-window] in counter:
                if counter[s2[i-window]] == 0:
                    matched -= 1
                counter[s2[i-window]] += 1
            if matched == len(counter):
                return True
        return False
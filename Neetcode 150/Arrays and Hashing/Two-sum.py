class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for i in s:
            if i in anagram:
                anagram[i] += 1
                continue
            anagram[i] = 1
        for j in t:
            if j in anagram and anagram[j] > 0:
                anagram[j] -= 1
            else:
                return False
        if list(anagram.values()) == [0]*len(anagram):
            return True
        else:
            return False
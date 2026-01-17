class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for i in strs:
            encode_str += str(len(i)) + '#' + i
        return encode_str 
    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decode_str = s[j+1:j+1+length]
            decode_list.append(decode_str)
            i = j+1+length
        return decode_list
            


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delim = s.find('#', i)
            length = int(s[i:delim])
            start = delim + 1
            res.append(s[start:start + length])
            i = start + length
        return res
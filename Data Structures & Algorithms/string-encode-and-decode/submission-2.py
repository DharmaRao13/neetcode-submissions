class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"asdfjkl#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        return s.split("asdfjkl#")[1:]

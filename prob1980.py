from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hash = {}

        for num in nums:
            hash[num] = 1

        lens = len(num)

        for i in range(1 << lens):
            if hash.get(f"{i:0{lens}b}") is None:
                return f"{i:0{lens}b}"

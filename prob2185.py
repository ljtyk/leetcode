from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        lens = len(pref)
        count = 0
        for word in words:
            if word[:lens] == pref:
                count +=1

        return count
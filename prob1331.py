from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort = sorted(set(arr))

        temp = []
        for i in range(len(arr)):
            temp.append(sort.index(arr[i]) + 1)

        return temp
from typing import Optional, List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def get_next_layer(leafs: List[TreeNode]):
            values: List[int] = []
            next_leafs: List[TreeNode] = []

            for leaf in leafs:
                values.append(leaf.val)
                if leaf.left:
                    next_leafs.append(leaf.left)
                if leaf.right:
                    next_leafs.append(leaf.right)

            return values, next_leafs

        def get_min_sort(nums: List[int]) -> int:
            sort: List[int] = sorted(nums)
            pos: Dict[int, int] = {}

            for i in range(len(nums)):
                pos[nums[i]] = i

            swap: int = 0
            for i in range(len(nums)):
                if sort[i] != nums[i]:
                    ind = pos[sort[i]]

                    nums[ind], nums[i] = nums[i], nums[ind]

                    pos[nums[i]] = i
                    pos[nums[ind]] = ind

                    swap += 1

            return swap

        layers = [root]
        swaped = 0

        while True:
            values, layers = get_next_layer(layers)
            if not values:
                break
            swaped += get_min_sort(values)

        return swaped
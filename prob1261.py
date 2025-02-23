# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.found = None

        def recursion(leaf: TreeNode):
            if leaf.left:
                leaf.left.val = 2 * leaf.val + 1
                recursion(leaf.left)
            if leaf.right:
                leaf.right.val = 2 * leaf.val + 2
                recursion(leaf.right)

        self.tree = root
        if self.tree.left or self.tree.right:
            self.tree.val = 0
            recursion(self.tree)

    def find(self, target: int) -> bool:
        self.found: bool = False

        if self.tree.val == target:
            self.found = True
            return self.found

        def recursion(leaf: TreeNode):
            if self.found:
                return
            if leaf.left:
                if leaf.left.val == target:
                    self.found = True
                    return
                else:
                    recursion(leaf.left)

            if leaf.right:
                if leaf.right.val == target:
                    self.found = True
                    return
                else:
                    recursion(leaf.right)

        recursion(self.tree)

        return self.found

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
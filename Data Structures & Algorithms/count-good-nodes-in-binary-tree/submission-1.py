# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.root_val = root.val
        def dfs(root, r_max):
            if not root:
                return
            if root.val >= r_max:
                self.result += 1
                r_max = root.val
            left = dfs(root.left, r_max)
            right = dfs(root.right, r_max)
        dfs(root, self.root_val)
        return self.result
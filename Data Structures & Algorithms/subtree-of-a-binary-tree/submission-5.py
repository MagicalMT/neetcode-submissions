# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_compare(r, s):
            if not r or not s:
                if r != s:
                    return False
                return True
            if r.val != s.val:
                return False
            left = dfs_compare(r.left, s.left)
            right = dfs_compare(r.right, s.right)
            return left and right

        def dfs_findsame(r, s):
            if not r:
                return False
            if r.val == s.val:
                if dfs_compare(r, s):
                    return True
            return dfs_findsame(r.left, s) or dfs_findsame(r.right, s)
        return dfs_findsame(root, subRoot)
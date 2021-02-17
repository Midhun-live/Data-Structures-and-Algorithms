# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.L = []
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            self.L.append(root.val)
            DFS(root.right)
        DFS(root)
        return self.L
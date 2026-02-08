# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            
            #An empty tree has height 0 and is balanced
            if not node:
                return 0

            #Recursively get left height, if left subtree is not balanced, return -1
            lh = height(node.left)
            if lh == -1:
                return -1

            #Recursively get right height, if right subtree is not balanced, return -1
            rh = height(node.right)
            if rh == -1:
                return -1

            #If the difference in height is more than 1, it's not balanced, return -1
            if abs(lh - rh) > 1:
                return -1

            #If balanced, return height of current node which is 1 + max of left and right heights
            result = 0
            return 1 + max(lh, rh)

        return height(root) != -1
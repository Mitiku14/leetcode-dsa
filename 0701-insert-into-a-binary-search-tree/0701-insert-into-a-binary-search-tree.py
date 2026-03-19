# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert(node, value):
            if node is None:
                return TreeNode(value)
            if node.val > value:
                node.left = insert(node.left, value)
            else:
                node.right = insert(node.right, value)
            
            return node
        
        return insert(root, val)
        
        
        
       
        


        
        

        

        

        
                

       



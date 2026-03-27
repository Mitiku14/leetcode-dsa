# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        root = postorder[n-1]
        stack = [TreeNode(root)]
        t = TreeNode(root)
        for i in range(n-2, -1, -1):
            child = TreeNode(postorder[i])
            cnt = 0

            while  stack and stack[-1].val == preorder[-1]:
                stack.pop()
                preorder.pop()
                cnt += 1
            if stack:
                par = stack[-1]
                t = par
            else:
                break 


            if cnt:
                par.left = child
                
            else:
                par.right = child

            
            stack.append(child)
        
        return stack[0]

        # if not preorder:
        #     return None
        # if len(preorder) == 1:
        #     return TreeNode(preorder[0])
        
        # root = TreeNode(preorder[0])
        # lef = postorder.index(preorder[1])


                     


#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        def traversal(root):
            if not root:
                return 
            output.append(root.val)       
            traversal(root.left)
            traversal(root.right)
            
        
        traversal(root)
        
        return output
        
# @lc code=end


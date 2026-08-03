# Recursive base case, if leaf is a leaf node see if root.vals (recursive cumulative) == targetSum. Recursively call left or right so if one leaf node returns true it overrides all false's returned
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum - root.val == 0
        
        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
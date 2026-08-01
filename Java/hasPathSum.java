class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        // Recursive base case, if leaf is a leaf node see if root.vals (recursive cumulative) == targetSum. Recursively call left or right so if one leaf node returns true it overrides all false's returned
        if (root == null) return false;

        if (root.left == null && root.right == null){
            return (targetSum - root.val == 0);
        }

        targetSum = targetSum - root.val;
            
        return (hasPathSum(root.left, targetSum) || hasPathSum(root.right, targetSum));
    }
}
/*
 * LeetCode 112 - Path Sum (Easy)
 *
 * Given the root of a binary tree and an integer targetSum, decide whether the
 * tree has any root-to-leaf path whose node values add up to exactly targetSum.
 *
 * A leaf is a node with no children, so the path has to run all the way from the
 * root down to a leaf - stopping partway through does not count. An empty tree has
 * no paths at all, so it returns false.
 *
 * Example: [5,4,8,11,null,13,4,7,2,null,null,null,1] with targetSum = 22  ->  true
 */

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
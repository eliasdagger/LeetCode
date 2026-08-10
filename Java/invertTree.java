/*
 * LeetCode 226 - Invert Binary Tree (Easy)
 *
 * Given the root of a binary tree, mirror it: swap the left and right child of
 * every node in the tree, from the root all the way down.
 *
 * Return the root of the mirrored tree. An empty tree returns null.
 *
 * Example: [4,2,7,1,3,6,9]  ->  [4,7,2,9,6,3,1]
 */

class Solution {
    public TreeNode invertTree(TreeNode root) {
        // add recursive base case, create a temp so we dont lose the connection from root to left, then change the pointers from left to right and vice versa, then call the same function resursively for each the left and right children to execute on the entire tree

        if (root == null) return null;

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.left);
        invertTree(root.right); 

        return root;
    }
}
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
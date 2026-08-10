/*
 * LeetCode 100 - Same Tree (Easy)
 *
 * Given the roots of two binary trees p and q, decide whether they are the same
 * tree. They only match if they have identical structure and every pair of
 * corresponding nodes holds the same value.
 *
 * Return true if they are identical, false otherwise. Two empty trees count as the
 * same tree.
 *
 * Example: [1,2,3] and [1,2,3]  ->  true
 *          [1,2] and [1,null,2]  ->  false (same values, different shape)
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // includes a recursive base case, checks if both nodes are present in either tree to see if they possess the same structure, returns the result of the comparison, then continues to recursively call.
        if (p == null && q == null){
            return true;
        }

        if ((p == null && q != null) || (p != null && q == null)){
            return false;
        }

        if (p.val == q.val){
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }

        else return false;
    }
}
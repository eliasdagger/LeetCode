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
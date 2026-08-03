import javax.swing.tree.TreeNode;

public class Solution {
    // null pointer are treated as 0, as we reach a new depth, it will be 1 more than its previous tree level, the recursive calls will continue incrementing count to 1, then the max value will be returned. 
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        return Math.max(1 + maxDepth(root.left), 1 + maxDepth(root.right));
    }
} {
    
}

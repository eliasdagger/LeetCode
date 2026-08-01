// Create a dynamic list of ints, create a helper method which recursively traverses the tree in order and adds the values to the list, then return the list.

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorder(root, res);
        return res;
    }
    
    private void inorder(TreeNode node, List<Integer> res){
        if (node == null) return;
        inorder(node.left, res);
        res.add(node.val);
        inorder(node.right, res);
    }
}
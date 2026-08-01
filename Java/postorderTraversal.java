// Create a dynamic list of ints, create a helper method which recursively traverses the tree post order (left, right, visit) and adds the values to the list, then return the list.

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<>();
        postorder(root, res);
        return res;
    }

    private void postorder(TreeNode node, ArrayList res){
        if (node == null) return;
        postorder(node.left, res);
        postorder(node.right, res);
        res.add(node.val);
    }
}
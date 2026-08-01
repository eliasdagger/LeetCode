// Create a dynamic list of ints, create a helper method which recursively traverses the tree pre order (visit, left, right) and adds the values to the list, then return the list.

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> res = new ArrayList();
        preorder(root, res);
        return res;
    }

    private void preorder(TreeNode node, ArrayList res){
        if (node == null) return;
        res.add(node.val);
        preorder(node.left, res);
        preorder(node.right, res);
    }
}
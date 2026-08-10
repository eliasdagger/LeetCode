// Include case for null list, create a queue since we will preorder traverse our tree then in the same order this will be the flattened list order
// then create a new tree with the queue values
class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;

        Deque<Integer> queue = new ArrayDeque<>();
        TreeNode curr = root;

        preorder(root, queue);
        queue.removeFirst();
        curr.left = null;
        curr.right = null;
        
        while (!queue.isEmpty()){
            curr.right = new TreeNode(queue.removeFirst());
            curr.left = null;
            curr = curr.right;
        }

    }

    private void preorder(TreeNode node, Deque queue){
        if (node == null) return;

        queue.addLast(node.val);
        preorder(node.left, queue);
        preorder(node.right, queue);
    }
}
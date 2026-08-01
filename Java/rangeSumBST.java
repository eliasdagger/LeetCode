class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        ArrayList<Integer> res = new ArrayList<>();
        inorder(root, res, low, high);
        int result = 0;

        for (int i = 0; i < res.size(); i++){
            result += res.get(i);
        }

        return result;
    }

    private void inorder(TreeNode node, ArrayList res, int low, int high){
        if (node == null) return;

        inorder(node.left, res, low, high);
        if (node.val <= high && node.val >= low){
            res.add(node.val);
        }

        inorder(node.right, res, low, high);
    }
}

public class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return 0;
        }

        int currentVal = (root.val >= low && root.val <= high) ? root.val : 0;

        int leftSum = rangeSumBST(root.left, low, high);
        int rightSum = rangeSumBST(root.right, low, high);

        return currentVal + leftSum + rightSum;
    }
}
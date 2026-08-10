/*
 * LeetCode 145 - Binary Tree Postorder Traversal (Easy)
 *
 * Given the root of a binary tree, return the values of its nodes in post-order:
 * for every node, visit its entire left subtree, then its entire right subtree,
 * and only then the node itself.
 *
 * Return the values as a list. An empty tree returns an empty list. The follow-up
 * asks whether you can do it iteratively instead of recursively.
 *
 * Example: 1 with right child 2, whose left child is 3  ->  [3,2,1]
 */

import java.util.*;

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
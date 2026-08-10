/*
 * LeetCode 144 - Binary Tree Preorder Traversal (Easy)
 *
 * Given the root of a binary tree, return the values of its nodes in pre-order:
 * for every node, visit the node itself first, then its entire left subtree, then
 * its entire right subtree.
 *
 * Return the values as a list. An empty tree returns an empty list. The follow-up
 * asks whether you can do it iteratively instead of recursively.
 *
 * Example: 1 with right child 2, whose left child is 3  ->  [1,2,3]
 */

import java.util.*;

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
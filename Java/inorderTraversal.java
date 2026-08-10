/*
 * LeetCode 94 - Binary Tree Inorder Traversal (Easy)
 *
 * Given the root of a binary tree, return the values of its nodes in in-order:
 * for every node, visit its entire left subtree, then the node itself, then its
 * entire right subtree.
 *
 * Return the values as a list. An empty tree returns an empty list. The follow-up
 * asks whether you can do it iteratively instead of recursively.
 *
 * Example: 1 with right child 2, whose left child is 3  ->  [1,3,2]
 */

import java.util.*;

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
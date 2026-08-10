/*
 * LeetCode 114 - Flatten Binary Tree to Linked List (Medium)
 *
 * Given the root of a binary tree, flatten it in place into a "linked list":
 *
 *   every node's right pointer becomes the next node in the list
 *   every node's left pointer becomes null
 *
 * The order has to match the tree's pre-order traversal - the node itself, then
 * its left subtree, then its right subtree. The method returns nothing, the tree
 * is rearranged where it sits, and an empty tree stays empty.
 *
 * The follow-up asks for O(1) extra space, meaning no queue and no recursion stack
 * holding the whole traversal at once.
 *
 * Example: [1,2,5,3,4,null,6]  ->  1->2->3->4->5->6, each linked as a right child
 */

import java.util.*;

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
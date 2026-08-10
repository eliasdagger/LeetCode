/*
 * LeetCode 237 - Delete Node in a Linked List (Medium)
 *
 * You are given a node in a singly linked list - not the head, just the node
 * itself - and you have no access to anything before it. Every value in the list
 * is unique, and the node you are handed is guaranteed not to be the last one.
 *
 * Delete that node. The method returns nothing; afterwards the list must read
 * exactly as it would if that node had never existed, one element shorter.
 *
 * The twist is that you cannot reach the previous node to reroute its pointer, so
 * you cannot unlink the node in the usual way. The only move available is to copy
 * the next node's value over the current one and drop the next node instead.
 *
 * Example: list 4->5->1->9, given the node holding 5  ->  4->1->9
 */

// To delete a node without having access to a previous pointer, we make the current node (the one we want to delete) the next nodes val, then disconnect the next node from the list.

class Solution {
    public void deleteNode(ListNode node) {
        ListNode n, curr;
        curr = node;
        n = curr.next;

        curr.val = n.val;
        curr.next = n.next;
        n.next = null;
    }
}
/*
 * LeetCode 206 - Reverse Linked List (Easy)
 *
 * Given the head of a singly linked list, reverse the direction of every link and
 * return the head of the reversed list.
 *
 * The reversal is done by rewiring the existing nodes, not by copying values into
 * a new list. An empty list or a single node comes back unchanged.
 *
 * Example: 1->2->3->4->5  ->  5->4->3->2->1
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode succ, curr, n;
        succ = null;
        curr = n = head;
        // set next to curr next since we will use a three pointer technique which will disconnect the link to the rest of the list, set curr to previous node then then shift succ to curr and curr to next, continue, this will reverse the list. Condition is while curr is not null bc this will iterate once more leaving succ as the last node, thus every node is reversed.
        while (curr != null){
            n = curr.next;
            curr.next = succ;
            succ = curr;
            curr = n;
        }

        return succ;
    }
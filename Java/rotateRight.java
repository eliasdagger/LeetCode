/*
 * LeetCode 61 - Rotate List (Medium)
 *
 * Given the head of a linked list, rotate the list to the right by k places -
 * each rotation moves the last node to the front - and return the new head.
 *
 * k can be far larger than the length of the list (up to 2 * 10^9), so
 * rotating one step at a time is too slow; only k modulo the length matters.
 * The list may also be empty or a single node.
 *
 * Example: 1->2->3->4->5, k = 2  ->  4->5->1->2->3
 *          0->1->2, k = 4        ->  2->0->1
 */

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // To rotate k to the right, create the list into a circular loop, then disconnect the loop on len of list - k then return the head of the list with a temp variable on knodes next
        if (head == null || k == 0 || head.next == null) return head;

        ListNode kNode, end;
        kNode = end = head;

        int len = 1;
        while (end.next != null){
            end = end.next;
            len++;
        }

        k = k % len;
        if (k == 0) return head;

        end.next = head;

        int rotate = len - k;
        for (int i = 1; i < rotate; i++){
            kNode = kNode.next;
        }
        
        ListNode res = kNode.next;
        kNode.next = null;
        return res;
    }
}
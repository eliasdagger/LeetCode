/*
 * LeetCode 876 - Middle of the Linked List (Easy)
 *
 * Given the head of a singly linked list, return the middle node itself - not just
 * its value, so everything after it comes along with it.
 *
 * If the list has an even number of nodes there are two middles, and the problem
 * asks specifically for the second one.
 *
 * Example: 1->2->3->4->5  ->  the node 3 (so 3->4->5)
 *          1->2->3->4->5->6  ->  the node 4 (so 4->5->6)
 */

class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode fast, slow;

        fast = slow = head;

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }
}
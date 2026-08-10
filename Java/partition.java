/*
 * LeetCode 86 - Partition List (Medium)
 *
 * Given the head of a linked list and a value x, reorder the list so that every
 * node with a value less than x comes before every node with a value greater than
 * or equal to x.
 *
 * The relative order of the nodes inside each of the two groups has to be
 * preserved - this is a stable partition, not a sort. Return the head of the
 * reordered list.
 *
 * Example: 1->4->3->2->5->2 with x = 3  ->  1->2->2->4->3->5
 */

class Solution {
    public ListNode partition(ListNode head, int x) {
        
        // create a dummy node to handle edge cases and simplify the logic, then another dummy node called temp, we will create a list of all nodes >= x, then removing them from our original list, then adding them in a while loop leading all values to be at the end in their original order. thus creating a partition 
        ListNode dummy = new ListNode(0);
        ListNode temp = new ListNode(0);
        dummy.next = head;

        ListNode prev, curr, t; 
        curr = head;
        prev = dummy;
        t = temp;

        while (curr != null) {
            if (curr.val >= x) {
                t.next = curr;
                t = t.next;

                prev.next = curr.next;

                curr.next = null;
                curr = prev.next;
            } else {
                prev = curr;
                curr = prev.next;  
            }
        }

        while (temp != null) {
            prev.next = temp.next;
            temp = temp.next;
            prev = prev.next;
        }

        return dummy.next;
    }
}
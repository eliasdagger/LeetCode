/*
 * LeetCode 2 - Add Two Numbers (Medium)
 *
 * You are given two non-empty linked lists, each representing a non-negative
 * integer with its digits stored in reverse order (the head is the ones digit).
 * Add the two numbers and return the sum as a linked list in the same format.
 *
 * The lists can have different lengths, and a carry can run past the end of
 * both lists, adding one extra node (99 + 1 = 100). Neither number has leading
 * zeros except the number 0 itself.
 *
 * Example: 2->4->3 and 5->6->4  ->  7->0->8   (342 + 465 = 807)
 *          9->9 and 1           ->  0->0->1   (99 + 1 = 100)
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Create a dummy and curr pointer, remainder int. 
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        int remainder = 0;

        // keep looping until we have no more numbers to handle. if the number is defined not null or 0, then we will add sum % 10, this will ensure we include always a single digit (ones place) in our new node. remainder is floor divison 10 will always be 0 or 1 since sum <= 20. 
        while (l1 != null || l2 != null || remainder != 0){
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;

            int sum = val1 + val2 + remainder;

            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            remainder = sum / 10;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        } 

        return dummy.next;
    }
}
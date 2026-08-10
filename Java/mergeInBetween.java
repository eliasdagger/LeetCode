/*
 * LeetCode 1669 - Merge In Between Linked Lists (Medium)
 *
 * You are given two linked lists, list1 and list2, and two integers a and b.
 *
 * Remove the nodes at positions a through b inclusive from list1 (0-indexed), then
 * splice the whole of list2 into the gap they leave behind. Return the head of the
 * resulting list.
 *
 * The problem guarantees a and b are valid positions well inside list1, so there
 * is always at least one node before index a and at least one after index b - the
 * head never changes and the tail never disappears.
 *
 * Example: list1 = 10->1->13->6->9->5, a = 3, b = 4,
 *          list2 = 1000000->1000001->1000002
 *       -> 10->1->13->1000000->1000001->1000002->5
 */

// Iterate to a, where prev pointer will connect to list2, curr pointer will retain our access to list1's removed section, iterate curr to the range of b-a + 1 to find the first node we want to keep again, then iterate to the end of list2,
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode dummy = new ListNode(0);
        dummy.next = list1;

        ListNode prev, curr;

        prev = dummy;
        curr = list1;
        
        for (int i = 0; i < a; i++){
            prev = curr;
            curr = prev.next;
        }

        prev.next = list2;
        
        for (int i = 0; i < b-a+1; i++){
            curr = curr.next;
        }

        while (prev.next != null){
            prev = prev.next;
        }

        prev.next = curr;

        return dummy.next;
    }
}
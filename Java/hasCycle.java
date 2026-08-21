/*
 * LeetCode 141 - Linked List Cycle (Easy)
 *
 * Given the head of a singly linked list, decide whether the list loops back on
 * itself. A cycle exists if following .next forever would revisit a node you have
 * already been on, instead of eventually reaching null.
 *
 * Return true if there is a cycle and false if the list terminates. The follow-up
 * asks you to do it using only O(1) extra space, so you cannot just store every
 * node you have visited.
 *
 * Example: 3->2->0->-4 where the last node points back at 2  ->  true
 */

public class hasCycle {
    // create a fast and slow pointer, the algo will be if they ever == there is a loop since they will land on the same node at one point
    // use fast as the conditions since it will reach null first if there is no loop, if there is no loop fast wont == slow and while loop will break thus returning false
    public boolean hasCycle(ListNode head) {
        ListNode fast, slow;
        fast = slow = head;
        while (fast != null){
            if (fast.next == null){
                return false;
            }
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow){
                return true;
            }

        }

        return false;
    }
}

// class Solution:
//     def hasCycle(self, head: Optional[ListNode]) -> bool:
//         slow = head
//         fast = head

//         while fast is not None:
//             if fast.next is None:
//                 return False

//             slow = slow.next
//             fast = fast.next.next

//             if slow == fast:
//                 return True

//         return False
/*
 * LeetCode 160 - Intersection of Two Linked Lists (Easy)
 *
 * Given the heads of two singly linked lists, return the node at which they
 * merge, or null if they never share a node. Intersection means the same node
 * object, not just an equal value - once the lists meet, every node after that
 * point is shared.
 *
 * The two lists can have different lengths before they meet, and neither list
 * has a cycle. Both lists must keep their original structure afterwards.
 *
 * The follow-up asks for O(m + n) time and O(1) extra memory.
 *
 * Example: A = 4->1->8->4->5, B = 5->6->1->8->4->5, sharing from 8  ->  node 8
 *          A = 2->6->4, B = 1->5, nothing shared                    ->  null
 */

public class getIntersectionNode {
    // Iterate through the lists until they equal, return the node. handles two different length lists since they swap heads makign them even, they will eventually reach the shared node, or null at the same time
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        ListNode pA = headA;
        ListNode pB = headB;

        while (pA != pB){
            pA = (pA == null) ? headB : pA.next;
            pB = (pB == null) ? headA : pB.next;
        }
        
        return pA;
    }
}
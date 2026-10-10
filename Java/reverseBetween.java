/*
 * LeetCode 92 - Reverse Linked List II (Medium)
 *
 * Given the head of a singly linked list and two positions left <= right
 * (1-indexed), reverse only the nodes from position left to position right and
 * return the head of the list. Everything outside that range stays in place.
 *
 * left can be 1, in which case the head of the list changes. left == right
 * means there is nothing to reverse.
 *
 * The follow-up asks you to do it in a single pass.
 *
 * Example: 1->2->3->4->5, left = 2, right = 4  ->  1->4->3->2->5
 *          5, left = 1, right = 1              ->  5
 */

class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // Include case for [] list or left == right thus one element is "reversed", rather itself
        if (head == null || left == right) return head;
        // Utilise a two pointer technique to set our bounds, find our bounds w a for loop, for l at left (same for right)
        // Utilise a stack to reverse order. 
        ListNode l, r;
        l = r = head;
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 1; i < left; i++) {
            l = l.next;
        }

        ListNode t = l;

        for (int i = 1; i < right; i++) {
            r = r.next;
        }

        for (int i = 0; i < right - left + 1; i++){
            stack.push(l.val);
            l = l.next;
        }

        while (!stack.isEmpty()) {
            t.val = stack.pop();
            t = t.next;
        }

        return head;
    }
}
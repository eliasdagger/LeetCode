/*
 * LeetCode 234 - Palindrome Linked List (Easy)
 *
 * Given the head of a singly linked list, decide whether the sequence of values
 * reads the same forwards and backwards.
 *
 * Return true if it is a palindrome, false otherwise. An empty list or a single
 * node is trivially a palindrome. The follow-up asks for O(n) time and O(1) extra
 * space, which rules out copying the whole list into an array or a stack.
 *
 * Example: 1->2->2->1  ->  true;   1->2  ->  false
 */

import java.util.ArrayDeque;
import java.util.Deque;
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        Deque<Integer> stack = new ArrayDeque<>();
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            stack.push(slow.val);
            slow = slow.next;
            fast = fast.next.next;
        }

        if (fast != null) {
            slow = slow.next;
        }

        while (slow != null) {
            if (stack.pop() != slow.val) {
                return false;
            }
            slow = slow.next;
        }

        return true;
    }
}
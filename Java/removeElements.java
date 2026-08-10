/*
 * LeetCode 203 - Remove Linked List Elements (Easy)
 *
 * Given the head of a linked list and an integer val, remove every node whose
 * value equals val and return the head of the new list.
 *
 * Matches can show up anywhere, including at the head itself or several in a row,
 * so the head you return may not be the head you were given. A dummy node in front
 * of the list makes every case look the same.
 *
 * Example: 1->2->6->3->4->5->6 with val = 6  ->  1->2->3->4->5
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) return null;
        head.next = removeElements(head.next, val);
        return head.val == val ? head.next : head;
    }
}

class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null){
            return null;
        }

        ListNode curr, prev;
        prev = null;
        curr = head;
    
        while (curr != null){
            if (curr.val == val){
                if (prev == null){
                    head = curr.next;
                    curr.next = null;
                    curr = head;
                } else {
                    prev.next = curr.next;
                    curr.next = null;
                    curr = prev.next;
                }
            } else {
                prev = curr;
                curr = curr.next;
            }
        }
        return head;
    }
}

// Cleaner iterative solution

class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode curr = head;
        ListNode prev = dummy;

        while (curr != null){
            if (curr.val == val){
                prev.next = curr.next;
                curr = prev.next;
            }
            else {
                prev = curr;
                curr = curr.next;
            }
        }
        
        return dummy.next;
    }
}
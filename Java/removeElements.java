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
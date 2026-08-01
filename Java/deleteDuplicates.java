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
    public ListNode deleteDuplicates(ListNode head) {
        // handle the simple case that the list is empty before we starting execution conditions this is a good practice to avoid null pointer exceptions and errors down the line
        if (head == null){
            return head;
        }
        // initialize two pointers to traverse the linked list, one for the current node and one for the successor node
        ListNode curr, succ;
        succ = head;
        curr = succ.next;
        // conditions is while curr is not null, 
        // first, if list is a single node, then we will simply return the current succ pointer (head). This will continue to remove duplicates until curr reaches the end of the list. This algorithm has a time complexity of O(n) since we are traversing the entire list once, and a space complexity of O(1) since we are using only a constant amount of extra space for the pointers.
        // succ node will point to currs next, then curr point to null thus removing the node. ending when curr is null allows for us to use curr.next. 
        // if values are not equal, shift pointers  
        while (curr != null){
            if(curr.val == succ.val){
                succ.next = curr.next;
                curr.next = null;
                curr = succ.next;
            }
            else {
                curr = curr.next;
                succ = succ.next;
            }
        }
        
        return head;
    }
}
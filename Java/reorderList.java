class Solution {
    public void reorderList(ListNode head) {
        // if our head is null, we should return an empty list before assigning elements to avoid null pointer exceptions

        if (head == null) return;

        // we will utilise a slow, fast pointer technique which will be used to find the middle of thelinked list. 
        ListNode slow, fast;
        slow = fast = head;

        // find the middle of the linked list, have the condition be while fast.next and fast.next.next to ensure be arent faced with null pointer exceptions. odd length linked will have slow pointer at the middle element, even length linked list will have slow pointer at the first of the two middle elements since the fast pointer will arrive at the second last pointer. 

        while (fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        // use three pointers to reverse the linked list while also disconnecting it from the main list creating a new list, next be be currs next, curr = prev node, having the next (n) pointer is because we have disconnected the list, then succ = curr, curr = n, 
        ListNode prev, curr; 
        prev = null;
        curr = slow.next;

        
        while (curr != null){
            ListNode n = curr.next;
            curr.next = prev;
            prev = curr;
            curr = n;
        }
        // disconnect the two lists

        slow.next = null;
        
        // make both point to the heads of the list
        ListNode head1, head2; 
        head1 = head;
        head2 = prev;
        
        // complete the "reordering" of the list
        while (head1 != null){
            ListNode n = head1.next;
            head1.next = head2;
            head1 = head2;
            head2 = n;
        }
    }
}
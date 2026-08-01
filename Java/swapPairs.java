class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node to handle edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode curr, prev, temp;
        prev = dummy; 
        curr = head;
        // Condition while curr is not null nor its next pointer is null will ensure that if there is an odd number of nodes, the last node will not be swapped
        // use a two pointer technique to swap nodes with a temp node, prev acts as the conductor where the two nodes after prev will be swapped and prev will updated to ensure the integrity of the linked list is maintained. 
        while (curr != null && curr.next != null){
            temp = curr.next;
            
            prev.next = temp;
            curr.next = temp.next;
            temp.next = curr;
            
            prev = curr;
            curr = prev.next;
        }
        return dummy.next;

        
        
        
    }
}
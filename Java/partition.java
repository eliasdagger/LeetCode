class Solution {
    public ListNode partition(ListNode head, int x) {
        
        // create a dummy node to handle edge cases and simplify the logic, then another dummy node called temp, we will create a list of all nodes >= x, then removing them from our original list, then adding them in a while loop leading all values to be at the end in their original order. thus creating a partition 
        ListNode dummy = new ListNode(0);
        ListNode temp = new ListNode(0);
        dummy.next = head;

        ListNode prev, curr, t; 
        curr = head;
        prev = dummy;
        t = temp;

        while (curr != null) {
            if (curr.val >= x) {
                t.next = curr;
                t = t.next;

                prev.next = curr.next;

                curr.next = null;
                curr = prev.next;
            } else {
                prev = curr;
                curr = prev.next;  
            }
        }

        while (temp != null) {
            prev.next = temp.next;
            temp = temp.next;
            prev = prev.next;
        }

        return dummy.next;
    }
}
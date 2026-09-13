class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Create a dummy and curr pointer, remainder int. 
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        int remainder = 0;

        // keep looping until we have no more numbers to handle. if the number is defined not null or 0, then we will add sum % 10, this will ensure we include always a single digit (ones place) in our new node. remainder is floor divison 10 will always be 0 or 1 since sum <= 20. 
        while (l1 != null || l2 != null || remainder != 0){
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;

            int sum = val1 + val2 + remainder;

            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            remainder = sum / 10;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        } 

        return dummy.next;
    }
}
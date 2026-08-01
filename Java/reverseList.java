class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode succ, curr, n;
        succ = null;
        curr = n = head;
        // set next to curr next since we will use a three pointer technique which will disconnect the link to the rest of the list, set curr to previous node then then shift succ to curr and curr to next, continue, this will reverse the list. Condition is while curr is not null bc this will iterate once more leaving succ as the last node, thus every node is reversed.
        while (curr != null){
            n = curr.next;
            curr.next = succ;
            succ = curr;
            curr = n;
        }

        return succ;
    }
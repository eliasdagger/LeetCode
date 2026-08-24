class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // To rotate k to the right, create the list into a circular loop, then disconnect the loop on len of list - k then return the head of the list with a temp variable on knodes next
        if (head == null || k == 0 || head.next == null) return head;

        ListNode kNode, end;
        kNode = end = head;

        int len = 1;
        while (end.next != null){
            end = end.next;
            len++;
        }

        k = k % len;
        if (k == 0) return head;

        end.next = head;

        int rotate = len - k;
        for (int i = 1; i < rotate; i++){
            kNode = kNode.next;
        }
        
        ListNode res = kNode.next;
        kNode.next = null;
        return res;
    }
}
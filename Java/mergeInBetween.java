// Iterate to a, where prev pointer will connect to list2, curr pointer will retain our access to list1's removed section, iterate curr to the range of b-a + 1 to find the first node we want to keep again, then iterate to the end of list2,
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode dummy = new ListNode(0);
        dummy.next = list1;

        ListNode prev, curr;

        prev = dummy;
        curr = list1;
        
        for (int i = 0; i < a; i++){
            prev = curr;
            curr = prev.next;
        }

        prev.next = list2;
        
        for (int i = 0; i < b-a+1; i++){
            curr = curr.next;
        }

        while (prev.next != null){
            prev = prev.next;
        }

        prev.next = curr;

        return dummy.next;
    }
}
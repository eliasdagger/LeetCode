
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode res = new ListNode(0);
    ListNode curr = res;
    while (list1 != null || list2 != null){
        if (list1 == null){
            while (list2 != null){
                curr.next = list2
                list2 = list2.next
            }
        }
        else if (list2 == null){
            while (list1 != null){
                curr.next = list1
                list1 = list1.next
            }
        }
        else{
            if (list1.val < list2.val){
                curr.next = list1;
                list1 = list1.next;
            }
            else if (list1.val > list2.val){
                curr.next = list2;
                list2 = list2.next;
            }
            else{
                curr.next = list1;
                curr.next = list2;
                list2 = list2.next;
                list1 = list1.next;
            }
        }
    }
    return res.next;
}

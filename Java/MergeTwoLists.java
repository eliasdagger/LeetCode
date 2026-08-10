/*
 * LeetCode 21 - Merge Two Sorted Lists (Easy)
 *
 * You are given the heads of two singly linked lists, list1 and list2, and both
 * lists are already sorted in non-decreasing order.
 *
 * Splice the two lists together into one sorted linked list by reusing the nodes
 * that already exist rather than building new ones, and return the head of the
 * result. Either list may be empty, in which case the answer is just the other one.
 *
 * Example: 1->2->4 and 1->3->4  ->  1->1->2->3->4->4
 */


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

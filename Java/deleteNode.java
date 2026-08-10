// To delete a node without having access to a previous pointer, we make the current node (the one we want to delete) the next nodes val, then disconnect the next node from the list.

class Solution {
    public void deleteNode(ListNode node) {
        ListNode n, curr;
        curr = node;
        n = curr.next;

        curr.val = n.val;
        curr.next = n.next;
        n.next = null;
    }
}
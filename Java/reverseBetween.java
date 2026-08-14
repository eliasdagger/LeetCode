class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // Include case for [] list or left == right thus one element is "reversed", rather itself
        if (head == null || left == right) return head;
        // Utilise a two pointer technique to set our bounds, find our bounds w a for loop, for l at left (same for right)
        // Utilise a stack to reverse order. 
        ListNode l, r;
        l = r = head;
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 1; i < left; i++) {
            l = l.next;
        }

        ListNode t = l;

        for (int i = 1; i < right; i++) {
            r = r.next;
        }

        for (int i = 0; i < right - left + 1; i++){
            stack.push(l.val);
            l = l.next;
        }

        while (!stack.isEmpty()) {
            t.val = stack.pop();
            t = t.next;
        }

        return head;
    }
}
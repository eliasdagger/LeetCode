/*
I am using the Floyd cycle finding algorithm, which is used to find the start of a cycle in a list

Here is how it is implemented: 
1. use the hare and tortoise technique with a fast and slow pointer
2. create a trigger for when they land on the same node
3. set slow to head
4. loop slow.next and fast.next until they match, they will land on the beginning of the cycle

Mathematical Proof: 
let x be the distance from the head to the start of the cycle 
let y be the distance from the start of the cycle to the collision point
let c be the length of the cycle

Distance traveled: 
slow = x + y         
fast = x + y + k * c     -> k is the number of loops completed

fast = slow * 2
x + y + k * c = 2(x + y)
x + y + k * c = 2x + 2y
k * c = x + y
k * c - y = x

stating that the distance from head to start of the cycle = number of cycles * length - start of cycle to collision
number of cycles in this case k, does influence the final reasoning/formula 

so x = c - y

*/

public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return null;
        ListNode slow, fast;
        slow = fast = head;

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;

            if (slow == fast) {
                slow = head;
                while (slow != fast){
                    slow = slow.next;
                    fast = fast.next;
                }

                return slow;
            }
        }

        return null;
    }
}
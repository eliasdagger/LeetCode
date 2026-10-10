/*
 * LeetCode 23 - Merge k Sorted Lists (Hard)
 *
 * You are given an array of k linked lists, each already sorted in ascending
 * order. Merge them all into one sorted linked list and return its head.
 *
 * k can be 0, and any of the individual lists can be empty. With up to 10^4
 * lists and 10^4 total nodes, the problem is about picking the smallest
 * current head out of k candidates efficiently, rather than repeatedly
 * scanning or rebuilding.
 *
 * Example: [1->4->5, 1->3->4, 2->6]  ->  1->1->2->3->4->4->5->6
 *          []                        ->  empty list
 *          [empty list]              ->  empty list
 */

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // Case for if there are no LL in lists
        if (lists.length == 0 || lists == null) return null;
        
        // Create a priority queue defining how the minHeap compares ListNode's by comparing their values
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.val, b.val)
        );
        
        // Append only heads of LL in lists, since it is in ascending order, we will have a minheap of 3 listnodes (if not null), then we can start at each LL 0 index
        for (ListNode node : lists){
            if (node != null) minHeap.add(node);
        }

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        // until minheap is empty, return the smallest head, add to our list, then we want to readd to our minheap, the head we just added, its next pointer to continue the loop throughout the rest of the LL
        while (!minHeap.isEmpty()){
            ListNode minVal = minHeap.poll();
            curr.next = minVal;
            curr = curr.next; 

            if (minVal.next != null){
                minHeap.add(minVal.next);
            }
        }

        return dummy.next;
    }
}


// MLE (memory limit exceeded)
        // if (lists == null || lists.length == 0) return null;

        // ListNode l1, l2, l3; 
        // l1 = lists[0];
        // l2 = lists[1];
        // l3 = lists[2];

        // ListNode dummy = new ListNode(0);
        // ListNode curr = dummy;

        // PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // while (l1 != null || l2 != null || l3 != null){
        //     int val1 = (l1 != null) ? l1.val : Integer.MAX_VALUE;
        //     int val2 = (l2 != null) ? l2.val : Integer.MAX_VALUE;
        //     int val3 = (l3 != null) ? l3.val : Integer.MAX_VALUE;
            
        //     minHeap.add(val1);
        //     minHeap.add(val2);
        //     minHeap.add(val3);

            
        // }

        // while (minHeap.peek() != null){
        //     int minVal = minHeap.poll();
        //     curr.next = new ListNode(minVal);
        //     curr = curr.next;
        // }

        // return dummy.next;


        // TLE (Time limit exceeded)
        // if (lists == null || lists.length == 0) return null;

        // ListNode l1, l2, l3; 
        // l1 = lists[0];
        // l2 = lists[1];
        // l3 = lists[2];

        // ListNode dummy = new ListNode(0);
        // ListNode curr = dummy;

        // while (l1 != null || l2 != null || l3 != null){
        //     int val1 = (l1 != null) ? l1.val : Integer.MAX_VALUE;
        //     int val2 = (l2 != null) ? l2.val : Integer.MAX_VALUE;
        //     int val3 = (l3 != null) ? l3.val : Integer.MAX_VALUE;

        //     PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        //     minHeap.add(val1);
        //     minHeap.add(val2);
        //     minHeap.add(val3);

        //     int minVal = minHeap.poll();
            
        //     curr.next = new ListNode(minVal);
        //     curr = curr.next;
        // }

        // return dummy.next;
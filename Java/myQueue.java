/*
 * LeetCode 232 - Implement Queue using Stacks (Easy)
 *
 * Implement a first-in-first-out queue using only two stacks. You may use nothing
 * but standard stack operations - push to the top, pop or peek at the top, check
 * the size, check whether it is empty.
 *
 * Implement the MyQueue class:
 *   MyQueue()     initializes the queue
 *   push(int x)   pushes x to the back of the queue
 *   pop()         removes and returns the element at the front
 *   peek()        returns the element at the front
 *   empty()       returns whether the queue is empty
 *
 * pop and peek are only ever called on a non-empty queue. The follow-up asks for
 * amortized O(1) per operation.
 */

class MyQueue {
    private int top;
    Deque<Integer> s1, s2;
    

    public MyQueue() {
        top = 0;
        s1 = new ArrayDeque<>();
        s2 = new ArrayDeque<>();
    }
    // To implement a queue using stacks, to ensure that we follow FIFO, we unload our current stack (s1) into s2, now the elements are accessible in an order which reflects the last added element is at the top of our stack, then we add a new 'last' element, then unload our stack into s1 which will flip the order to the first in, will be the first out when pop is called. 
    public void push(int x) {
        while (!s1.isEmpty()){
            s2.addLast(s1.removeLast());
        }

        s2.addLast(x);

        while (!s2.isEmpty()){
            s1.addLast(s2.removeLast());
        }

        top++;
    }
    
    public int pop() {
        top--;
        return s1.removeLast();
    }
    
    public int peek() {
        return s1.peekLast();
    }
    
    public boolean empty() {
        return (top == 0);
    }
}
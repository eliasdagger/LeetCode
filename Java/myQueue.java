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
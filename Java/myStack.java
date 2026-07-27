class MyStack {
    private int top;
    Deque<Integer> q1, q2;

    public MyStack() {
        top = 0;
        q1 = new ArrayDeque<>();
        q2 = new ArrayDeque<>();
    }
    // to create a stack using queues, we enqueue our pushed value to q2 then enqueue q1 and dequeue until its empty, this way the element we push will be the first out, as the elements previously pushed will be enqueued behind this val, ultimately mimicking a stacks characteristics.  
    public void push(int x) {
        q2.addLast(x);

        while (!q1.isEmpty()){
            q2.addLast(q1.removeFirst());
        }
        Deque<Integer> temp = q1;

        top++;
        q1 = q2;
        q2 = temp;
    }
    
    public int pop() {
        top--;
        return q1.removeFirst();
    }
    
    public int top() {
        return q1.peekFirst();
    }
    
    public boolean empty() {
        return (top == 0);
    }
}

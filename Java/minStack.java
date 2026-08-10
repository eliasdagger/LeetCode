/*
 * LeetCode 155 - Min Stack (Medium)
 *
 * Design a stack that supports the usual operations plus retrieving the smallest
 * value currently in it, with every operation running in O(1) time.
 *
 * Implement the MinStack class:
 *   MinStack()      initializes an empty stack
 *   push(int val)   pushes val onto the stack
 *   pop()           removes the element on top
 *   top()           returns the element on top
 *   getMin()        returns the minimum element currently in the stack
 *
 * pop, top and getMin are only ever called on a non-empty stack.
 *
 * getMin is the whole difficulty: scanning the stack for the minimum is O(n), so
 * you need to carry the running minimum along with the values as you push.
 */

class MinStack {

    private int top;
    private int[] arr;
    private int[] minArr;

    public MinStack() {
        top = 0;
        arr = new int[30001];
        minArr = new int[30001];
    }
    
    public void push(int val) {
        arr[top] = val;
        if (top == 0) {
            minArr[top] = val;
        } else {
            minArr[top] = Math.min(val, minArr[top - 1]);
        }
        top++;
    }
    
    public void pop() {
        top--;
    }
    
    public int top() {
        return arr[top - 1];
    }
    
    public int getMin() {
        return minArr[top - 1];
    }
}

class MinStack {

    private int top;
	private int[] arr;

    public MinStack() {
        top = 0;
        arr = new int[0];

    }
    
    public void push(int val) {

        int[] temp = new int[top + 1];
        
        if (top == 0){
    		temp[top] = val;
    	}else {
    		for (int i = 0; i < temp.length - 1; i++){
                temp[i] = arr[i];
            }

            temp[temp.length - 1] = val;
    	}
        
        arr = temp;
        
        top++;
    }
    
    public void pop() {
        top--;

        int[] temp = new int[top];

        for (int i = 0; i < top; i++){
            temp[i] = arr[i];
        }

        arr = temp;
    }
    
    public int top() {
        return arr[top - 1];
    }
    
    public int getMin() {
        if (top == 0){
            return -1;
        }

        int min = arr[0];

        for (int i = 0; i < top; i++){
            if (arr[i] < min){
                min = arr[i];
            }
        }

        return min;
    }
}

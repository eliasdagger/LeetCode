/* Allocate enough memory so we dont run into collisions (0 <= key, value <= 106).
   Fill with a default value of -1, this value wont be used by LeetCode (0 <= key, value <= 106) so return -1 if key:value doesnt exist requires trivial sol. 
 */

import java.util.Arrays;

class MyHashMap {
    private int[] dct;



    public MyHashMap() {
        dct = new int[1000001];
        Arrays.fill(dct, -1);
    }
    
    public void put(int key, int value) {
        dct[key] = value;
    }
    
    public int get(int key) {
        return dct[key];
    }
    
    public void remove(int key) {
        dct[key] = -1;
    }
}
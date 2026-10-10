/*
 * LeetCode 706 - Design HashMap (Easy)
 *
 * Build a hash map from scratch, without any built-in hash table library. The
 * class supports put(key, value), which inserts or overwrites a mapping;
 * get(key), which returns the mapped value or -1 if the key is absent; and
 * remove(key), which deletes the mapping if it exists.
 *
 * Keys and values are both in the range 0 <= key, value <= 10^6, and there are
 * at most 10^4 calls in total. The small key range is what makes a plain
 * direct-address array viable; the general version handles collisions with
 * buckets instead.
 *
 * Example: put(1,1), put(2,2), get(1) -> 1, get(3) -> -1, put(2,1),
 *          get(2) -> 1, remove(2), get(2) -> -1
 */

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

/**
 * 
 * 
 * 
 * MyHashMap - C Implementation

First create the blueprint for MyHashMap, saying an array of 1000001 indeces is its characteristics
Create the hashmap in memory by using malloc, which creates memory of sizeof HashMap, then returns its address, this reference is stored in obj*
Use memset to fill sizeof(obj's array) -1's into obj's arr 
free() releases the memory stored from malloc

typedef struct {
    int arr[1000001];
} MyHashMap;


MyHashMap* myHashMapCreate() {
    MyHashMap* obj = malloc(sizeof(MyHashMap));
    memset(obj->arr, -1, sizeof(obj->arr));
    return obj;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    obj->arr[key] = value;
}

int myHashMapGet(MyHashMap* obj, int key) {
    return obj->arr[key];
}

void myHashMapRemove(MyHashMap* obj, int key) {
    obj->arr[key] = -1;
}

void myHashMapFree(MyHashMap* obj) {
    free(obj);
}
 */
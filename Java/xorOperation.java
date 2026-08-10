/*
 * LeetCode 1486 - XOR Operation in an Array (Easy)
 *
 * You are given two integers n and start. Picture an array nums of length n where
 *
 *   nums[i] = start + 2 * i
 *
 * so the values climb from start in steps of two. You are never handed the array
 * itself - only n and start, and you build it as you go.
 *
 * Return the bitwise XOR of every element of nums.
 *
 * Example: n = 5, start = 0  ->  nums = [0,2,4,6,8], and 0^2^4^6^8 = 8
 *          n = 4, start = 3  ->  nums = [3,5,7,9], and 3^5^7^9 = 8
 */

// ^= will have x * x = 0 and x * 0 = x

class Solution {
    public int xorOperation(int n, int start) {
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans ^= (start + 2 * i);
        }
        return ans;
    }
}
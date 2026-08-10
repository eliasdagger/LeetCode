/*
 * LeetCode 2769 - Find the Maximum Achievable Number (Easy)
 *
 * You are given two integers num and t. An integer x is called achievable if you
 * can make x and num equal by applying the following operation at most t times:
 *
 *   increase or decrease x by 1, and at the same time increase or decrease num by 1
 *
 * Return the largest achievable x.
 *
 * Each operation can close a gap of 2 - move num up one while moving x down one -
 * so t operations can bridge a gap of 2t.
 *
 * Example: num = 4, t = 1  ->  6
 */

class Solution {
    public int theMaximumAchievableX(int num, int t) {
        // To achieve max x, the increments are inversly proportional to 1 for x and nums, thus each increment will account for 2, max number achievable is num + t*2
        return num + (t * 2);
    }
}
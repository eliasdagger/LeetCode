class Solution {
    public int theMaximumAchievableX(int num, int t) {
        // To achieve max x, the increments are inversly proportional to 1 for x and nums, thus each increment will account for 2, max number achievable is num + t*2
        return num + (t * 2);
    }
}
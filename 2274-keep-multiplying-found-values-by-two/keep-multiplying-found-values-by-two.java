class Solution {
    public int findFinalValue(int[] nums, int n) {
        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);}
        
        while (numSet.contains(n)) {
            n *= 2;}
        
        return n;}
}
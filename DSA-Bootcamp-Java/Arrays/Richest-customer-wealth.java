import java.util.Arrays;

class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for (int i = 0; i < accounts.length; i++) {
            max = Math.max(Arrays.stream(accounts[i]).sum(), max);
        }
        return max;
    }
}
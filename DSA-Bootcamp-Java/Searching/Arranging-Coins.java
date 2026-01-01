class Solution {
    public int arrangeCoins(int n) {
        int start = 1;
        int end = n;
        int maxrows = 0;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            long val = (long) mid * (mid + 1) / 2;

            if (val == n) {
                return mid;
            } else if (val < n) {
                maxrows = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return maxrows;
    }
}

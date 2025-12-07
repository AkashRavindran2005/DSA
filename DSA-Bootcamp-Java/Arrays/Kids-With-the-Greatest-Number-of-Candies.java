import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxnum = 0;
        for (int c : candies) {
            if (c > maxnum)
                maxnum = c;
        }
        List<Boolean> ans = new ArrayList<>();
        for (int c : candies) {
            ans.add(c + extraCandies >= maxnum);
        }
        return ans;
    }
}

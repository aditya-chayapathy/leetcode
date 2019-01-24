class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }

        int[] count = new int[s.length() + 1];
        count[0] = 1;
        if (s.charAt(0) != '0') {
            count[1] = 1;
        } else {
            count[1] = 0;
        }

        for(int i = 2; i <= s.length(); i++) {
            int prev = Integer.valueOf(s.substring(i-1, i));
            int prev2 = Integer.valueOf(s.substring(i-2, i));
            if(prev2 >= 10 && prev2 <= 26) {
                count[i] += count[i-2];
            }
            if(prev >= 1 && prev <= 9) {
                count[i] += count[i-1];
            }
        }
        return count[s.length()];
    }
}
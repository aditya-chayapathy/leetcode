class Solution {
    public String countAndSay(int n) {
        String solution = "1";
        if(n == 1) {
            return solution;
        }
        for (int i=2; i<=n; i++){
            String solutionCopy = solution;
            solution = "";
            int j=0;
            int k=0;
            while(true) {
                if (solutionCopy.charAt(j) == solutionCopy.charAt(k)) {
                    k++;
                }
                if (k == solutionCopy.length()) {
                    solution += (k - j) + "" + solutionCopy.charAt(k - 1);
                    break;
                }
                if (solutionCopy.charAt(j) != solutionCopy.charAt(k)) {
                    solution += (k - j) + "" + solutionCopy.charAt(k - 1);
                    j = k;
                }
            }
        }
        return solution;
    }

}
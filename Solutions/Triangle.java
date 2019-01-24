class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[][] triangleMatrix = new int[triangle.size()][triangle.size()];
        for (int i=0; i<triangle.size(); i++) {
            for (int j=0; j<triangle.size(); j++) {
                triangleMatrix[i][j] = 0;
            }
        }

        for (int i=0; i<triangle.size(); i++) {
            for (int j=0; j<triangle.get(i).size(); j++) {
                triangleMatrix[i][j] = triangle.get(i).get(j);
            }
        }

        for (int i=triangle.size() - 2; i>=0; i--)
        {
            for (int j=0; j<=i; j++)
            {
                if (triangleMatrix[i+1][j] > triangleMatrix[i+1][j+1])
                    triangleMatrix[i][j] += triangleMatrix[i+1][j+1];
                else
                    triangleMatrix[i][j] += triangleMatrix[i+1][j];
            }
        }

        return triangleMatrix[0][0];
    }
}
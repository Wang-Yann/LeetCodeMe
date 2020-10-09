//
/* Created by rock on 5/8/20.
*/

#include "leetcode_functions.h"

int maximalSquare(char **matrix, int matrixSize, int *matrixColSize) {
    if (matrixSize == 0) {
        return 0;
    }
//    //创建dp数组并初始化
//    int **dp = (int **)calloc(matrixSize*matrixColSize[0], sizeof(int*));
//    int temp = 0;
//    for (int i = 0; i < matrixSize; i++){
//        dp[i] = (int *)calloc(matrixColSize[i], sizeof(int));
//    }
//    int ret = 0;

//    for (int i = 0; i < matrixSize; ++i) {
//        printf("%s\n", matrix[i]);
//    }
    int colsSize = matrixColSize[0];
    int dp[matrixSize][colsSize];
    memset(dp, 0, sizeof(dp));
    int j, k;
    int ms = 0;
    for (j = 0; j < matrixSize; j++) {
        for (k = 0; k < colsSize; k++) {
//            printf("%c  j %d k %d\n", matrix[j][k],j,k);
            if (matrix[j][k] == '1' && j > 0 && k > 0) {
                dp[j][k] = MIN(dp[j - 1][k], dp[j][k - 1], dp[j - 1][k - 1]) + 1;
            }
            if (dp[j][k] > ms) {
                ms = dp[j][k];
            }
        }
    }
    return ms * ms;


}


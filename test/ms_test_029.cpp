//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(spiralOrder, test1) {
    int m[3][3] = {{1, 2, 3},
                   {4, 5, 6},
                   {7, 8, 9}};
    int *matrix[3];
    for (int i = 0; i < 3; i++) {
        matrix[i] = m[i];
    }
    int matrixSize = 3;
    int matrixColSize[] = {3,3,3};
    int returnSize;
    int expected[] = {1, 2, 3, 6, 9, 8, 7, 4, 5};
    int* res = spiralOrder(matrix, matrixSize, matrixColSize, &returnSize);
    ASSERT_EQ(returnSize, matrixSize * matrixColSize[0]);
    for (int i = 0; i < returnSize; ++i) {
        ASSERT_EQ(*(res + i), expected[i]);
    }
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize)
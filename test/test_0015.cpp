//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(threeSum, test1) {
    int nums[] = {-1, 0, 1, 2, -1, -4};
    int numSize = 6;
    int returnSize;
    int **returnColumnSizes = (int **) malloc(sizeof(int *) * 6);;
    int **res;

    int arr1[] = {-1, -1, 2};
    int arr2[] = {-1, 0, 1};
    int *expected[] = {arr1, arr2};
    res = threeSum(nums, numSize, &returnSize, returnColumnSizes);

    ASSERT_EQ(returnSize, 2);
    for (int i = 0; i < returnSize; i++) {
        int columnSize = (*returnColumnSizes)[i];
        ASSERT_EQ(columnSize, 3);
        for (int j = 0; j < columnSize; j++) {
            printf("Return: %d\n", res[i][j]);
            ASSERT_EQ(res[i][j], expected[i][j]);
        }
    }
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
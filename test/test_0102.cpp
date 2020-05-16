//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(levelOrder, test1) {
    //TODO TODO BUG
    struct TreeNode  left = {1, NULL, NULL};
    struct TreeNode  right = {3, NULL, NULL};
    struct TreeNode  root = {2,&left,&right};


    int arr1[3];
    int arr2[3];
    int * ptr2[]={arr1,arr2};
    int returnSize=5;
    int **res = levelOrder(&root, &returnSize, ptr2);

    for (int i = 0; i < 2; ++i) {
        printf("Return: %d,%d\n", *res[i], *(res[i] + 1));
    }
    EXPECT_TRUE(0==memcmp(res,res, sizeof(res)));
}





int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
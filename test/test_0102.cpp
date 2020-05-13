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
    int tmp1[] = {1};
    int tmp2[] = {3,2};
    int * pairs[2] = {tmp1,tmp2};


    int *returnSize;
    int **returnColumnSizes;
    int **res = levelOrder(&root, returnSize, returnColumnSizes);

//    for (int i = 0; i < 2; ++i) {
//        printf("Return: %d,%d",*pairs[i],*(pairs[i]+1));
//    }
    EXPECT_TRUE(0==memcmp(res,pairs, sizeof(pairs)));
}





int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(isValidBST, test1) {
    struct TreeNode  left = {1, NULL, NULL};
    struct TreeNode  right = {3, NULL, NULL};
    struct TreeNode  root = {2,&left,&right};
    ASSERT_TRUE(isValidBST(&root));
}

TEST(isValidBST, test2) {
    struct TreeNode  left = {1, NULL, NULL};
    struct TreeNode  right;
    right.val = 3;
    struct TreeNode  root = {2,&left,&right};
    ASSERT_TRUE(isValidBST(&root));
}


TEST(isValidBST, test3) {
    struct TreeNode  left = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode  right = {
            .val=3,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode  root = {
            val:2,
            left:&left,
            right:&right,
    };
    ASSERT_TRUE(isValidBST(&root));
}


//
//int main(int argc, char **argv) {
//    ::testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
//}
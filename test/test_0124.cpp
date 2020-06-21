//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(maxPathSum, test1) {
    struct TreeNode  left = {1, NULL, NULL};
    struct TreeNode  right = {3, NULL, NULL};
    struct TreeNode  root = {2,&left,&right};
    ASSERT_EQ(maxPathSum(&root),6);
}


TEST(maxPathSum, test2) {
    struct TreeNode  leftleft = {
            .val=100,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode  leftright = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode  left = {
            .val=1,
            .left=&leftleft,
            .right=&leftright
    };
    struct TreeNode  right = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode  root = {
            val:2,
            left:&left,
            right:&right,
    };
    ASSERT_EQ(maxPathSum(&root),104);
}



int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
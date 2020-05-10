//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(lowestCommonAncestor, test1) {
    struct TreeNode left = {1, NULL, NULL};
    struct TreeNode right = {3, NULL, NULL};
    struct TreeNode root = {2, &left, &right};
    struct TreeNode *res = lowestCommonAncestor(&root, &left, &right);
    ASSERT_EQ(res, &root);

}


TEST(lowestCommonAncestor, test3) {
    struct TreeNode left = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode right = {
            .val=3,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode root = {
            val:2,
            left:&left,
            right:&right,
    };
    struct TreeNode *res = lowestCommonAncestor(&root, &left, &right);
    ASSERT_EQ(res->val, root.val);

}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

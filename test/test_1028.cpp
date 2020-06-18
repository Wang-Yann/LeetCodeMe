//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(recoverFromPreorder, test3) {
    struct TreeNode t3 = {
            .val=3,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode t4 = {
            .val=4,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode t6 = {
            .val=6,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode t7 = {
            .val=7,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode t2 = {
            .val=2,
            .left = &t3,
            .right=&t4
    };
    struct TreeNode t5 = {
            .val=5,
            .left = &t6,
            .right=&t7
    };
    struct TreeNode root = {
            1, &t2, &t5
    };

    char *S = "1-2--3--4-5--6--7";

    struct TreeNode *res = recoverFromPreorder(S);
    //    ASSERT_TRUE(checkTreeEqual(res, res));
    ASSERT_TRUE(checkTreeEqual(res, &root));
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

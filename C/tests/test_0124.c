//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(test_0124) {
    struct TreeNode leftleft = {
            .val=100,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode leftright = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode left = {
            .val=1,
            .left=&leftleft,
            .right=&leftright
    };
    struct TreeNode right = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode root = {
            val:2,
            left:&left,
            right:&right,
    };
    ck_assert_uint_eq(maxPathSum(&root), 104);
}

//TEST(maxPathSum, test1) {
//struct TreeNode  left = {1, NULL, NULL};
//struct TreeNode  right = {3, NULL, NULL};
//struct TreeNode  root = {2,&left,&right};
//ck_assert_uint_eq(maxPathSum(&root),6);
//}
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("test_0124");       // 建立Suite
    TCase *tc_add = tcase_create("test_0124");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, test_0124);     // 测试用例加到测试集中
    return s;
}



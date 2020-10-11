//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(tt_1028)
    {
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
        //    ck_assert(checkTreeEqual(res, res));
        ck_assert(checkTreeEqual(res, &root));
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("tt_1028");       // 建立Suite
    TCase *tc_add = tcase_create("tt_1028");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, tt_1028);     // 测试用例加到测试集中
    return s;
}


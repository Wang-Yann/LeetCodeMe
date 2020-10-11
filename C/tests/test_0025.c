//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_reverseKGroup)
    {
        int n = 2;
        struct ListNode nodes[5];
        int i;
        int nums[5] = {1, 2, 3, 4, 5};
        int resNums[5] = {2, 1, 4, 3, 5};
        ListNode *head = initNodeList(nums, 5);
        ListNode *expected = initNodeList(resNums, 5);
        ListNode *res = reverseKGroup(head, n);
        ck_assert(checkListEqual(res, expected));
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_reverseKGroup");       // 建立Suite
    TCase *tc_add = tcase_create("t_reverseKGroup");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_reverseKGroup);     // 测试用例加到测试集中
    return s;
}

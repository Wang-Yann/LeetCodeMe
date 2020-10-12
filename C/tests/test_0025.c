//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_reverseKGroup)
    {
        int n = 2;
        int nums[4] = {1, 2, 3, 4};
        int resNums[4] = {2, 1, 4, 3};
        ListNode *head = initNodeList(nums, 4);
        ListNode *expected = initNodeList(resNums, 4);
        ListNode *res = reverseKGroup(head, n);
        while (expected != NULL) {
            printf("%d", expected->val);
            expected = expected->next;
        }
        fputs("---------------------------",stdout);
        while (res != NULL) {
            printf("%d", res->val);
            res = res->next;
        }
        fputs("---------------------------",stdout);
        ck_assert(checkListEqual(res, expected));
    }
END_TEST

START_TEST(t_reverseKGroup1)
    {


        int n = 2;
        int resNums[5] = {2, 1, 4, 3, 6};
        ListNode n5 = {6,NULL};
        ListNode n4 = {4,&n5};
        ListNode n3 = {3,&n4};
        ListNode n2 = {2,&n3};
        ListNode head = {1,&n2};
        ListNode *expected = initNodeList(resNums, 5);
        ListNode *res = reverseKGroup(&head, n);
        while (expected != NULL) {
            printf("%d", expected->val);
            expected = expected->next;
        }
        fputs("---------------------------",stdout);
        while (res != NULL) {
            printf("%d", res->val);
            res = res->next;
        }
        fputs("---------------------------",stdout);
        ck_assert(checkListEqual(res, expected));
    }
END_TEST


Suite *make_a_suite() {
    Suite *s = suite_create("t_reverseKGroup");       // 建立Suite
    TCase *tc_add = tcase_create("t_reverseKGroup");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_reverseKGroup);     // 测试用例加到测试集中
    tcase_add_test(tc_add, t_reverseKGroup1);     // 测试用例加到测试集中
    return s;
}

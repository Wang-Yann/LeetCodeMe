//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(tt_1371)
    {
        char s1[] = "eleetminicoworoep";
        char s2[] = "leetcodeisgreat";
        char *s3 = "bcbcbc";
        ck_assert_uint_eq(findTheLongestSubstring(s1),13);
        ck_assert_uint_eq(findTheLongestSubstring(s2),5);
        ck_assert_uint_eq(findTheLongestSubstring(s3),6);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("tt_1371");       // 建立Suite
    TCase *tc_add = tcase_create("tt_1371");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, tt_1371);     // 测试用例加到测试集中
    return s;
}

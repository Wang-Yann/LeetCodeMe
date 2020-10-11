//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0394)
    {
        char s1[] ="3[a2[c]]";
        char expected[] = "accaccacc";
        char *res = decodeString(s1);

        ck_assert(strcmp(expected,res)==0);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0394");       // 建立Suite
    TCase *tc_add = tcase_create("t_0394");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0394);     // 测试用例加到测试集中
    return s;
}


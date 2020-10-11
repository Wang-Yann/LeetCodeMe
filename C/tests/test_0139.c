//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0139) {
    char s1[] = "leetcode";
    char *wordDict1[] = {"leet", "code"};
    bool result1 = wordBreak(s1, wordDict1,
                             sizeof(wordDict1) / sizeof(char *));
    ck_assert(result1);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0139");       // 建立Suite
    TCase *tc_add = tcase_create("t_0139");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0139);     // 测试用例加到测试集中
    return s;
}

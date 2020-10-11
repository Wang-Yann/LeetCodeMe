//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(test_str1)
    {
        char name[100];
        char *description;

        strcpy(name, "Zara Ali");

        /* 动态分配内存 */
        description = (char *) malloc(200 * sizeof(char));
        if (description == NULL) {
            fprintf(stderr, "Error - unable to allocate required memory\n");
        } else {
            strcpy(description, "Zara ali a DPS student in class 10th");
        }
        printf("Name = %s\n", name);
        printf("Description: %s\n", description);
                fail_unless(2 + 3 == 5, "error, 2 + 3 != 5");
    }

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("test_str1");       // 建立Suite
    TCase *tc_add = tcase_create("test_str1");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, test_str1);     // 测试用例加到测试集中
    return s;
}

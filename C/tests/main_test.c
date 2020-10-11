/**
 * @Author         : Rock Wayne  
 * @Created        : 2020-10-10 01:40.
 * @Email          : lostlorder@gamil.com
 * @Description    : test_main.c	
 
*/
#include <stdlib.h>
#include "units_all.h"

int main(void)
{
    int number_failed;
    SRunner *sr;
    Suite * s = make_a_suite();
    sr = srunner_create(s);//把Suite加入到SRunner里面
    srunner_run_all(sr, CK_VERBOSE);//运行所有测试用例
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 1) ? EXIT_SUCCESS : EXIT_FAILURE;
}

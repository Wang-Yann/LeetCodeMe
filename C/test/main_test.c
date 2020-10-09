/**
 * @Author         : Rock Wayne  
 * @Created        : 2020-10-10 01:40.
 * @Email          : lostlorder@gamil.com
 * @Description    : test_main.c	
 
*/

#include "units_all.h"

int main(void)
{
    int n;
    SRunner *sr;
    sr = srunner_create(make_a_suite());//把Suite加入到SRunner里面
    srunner_run_all(sr, CK_NORMAL);//运行所有测试用例
    n = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (n==0)? EXIT_SUCCESS: EXIT_FAILURE;
}

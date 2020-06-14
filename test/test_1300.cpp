//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(findBestValue, test1) {
    int arr[] = {60864,25176,27249,21296,20204};
    int target=56803;
    int result = findBestValue(arr, sizeof(arr) / sizeof(int),target);

    ASSERT_EQ( result,11361);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

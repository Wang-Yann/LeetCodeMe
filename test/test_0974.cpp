//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(subarraysDivByK, test1) {
    int nums[] = {4,5,0,-2,-3,1};
    int result = subarraysDivByK(nums, sizeof(nums) / sizeof(int),5);

    ASSERT_EQ( result,7);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

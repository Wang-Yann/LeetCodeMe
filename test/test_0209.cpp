//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(minSubArrayLen, test1) {
    int nums[] = {2,3,1,2,4,3};
    int s=7;
    int result = minSubArrayLen(s,nums, sizeof(nums) / sizeof(int));
    ASSERT_EQ( result,2);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

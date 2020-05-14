//
/* Created by rock on 5/14/20.
*/

int singleNumber(int *nums, int numsSize) {
    int res = 0;
    for (int i = 0; i < numsSize; ++i) {
        res ^= *(nums + i);
    }
    return res;
}
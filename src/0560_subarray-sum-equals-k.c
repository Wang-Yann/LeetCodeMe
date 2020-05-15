//
/* Created by rock on 5/15/20.
*/

int subarraySum(int* nums, int numsSize, int k){
    int ans = 0;
    int i, sum;
    while (numsSize >= 0) {
        sum = 0;
        i = 0;
        while (i < numsSize) {
            sum += nums[i];
            if (sum == k) {
                ans++;
            }
            i++;
        }
        numsSize--;
        nums++;
    }
    return ans;


}
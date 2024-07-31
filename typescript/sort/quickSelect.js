function findKthLargest(nums, k) {
    var kk = nums.length - k;
    var anss = null;
    function quickSelect(l, r) {
        var pivot = nums[r];
        var p = l;
        for (var i = l; i < r; i++) {
            if (nums[i] < pivot) {
                nums[p], nums[i] = nums[i], nums[p];
                p++;
            }
        }
        nums[p], nums[r] = nums[r], nums[p];
        if (p > kk) {
            quickSelect(l, p - 1);
        }
        else if (p < kk) {
            quickSelect(p + 1, r);
        }
        else {
            anss = nums[p];
            return nums[p];
        }
    }
    quickSelect(0, nums.length - 1);
    return anss;
}
;
var b = findKthLargest([1, 2, 4, 5, 6, 5, 6], 6);
console.log(b);

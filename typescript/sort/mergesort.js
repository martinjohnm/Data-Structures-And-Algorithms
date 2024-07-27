function mergeSort(array) {
    if (array.length <= 1) {
        return array;
    }
    var middle = Math.floor(array.length / 2);
    var leftHalf = array.slice(0, middle);
    var rightHalf = array.slice(middle);
    return merge(mergeSort(leftHalf), mergeSort(rightHalf));
}
function merge(left, right) {
    var result = [];
    var leftIndex = 0;
    var rightIndex = 0;
    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            result.push(left[leftIndex]);
            leftIndex++;
        }
        else {
            result.push(right[rightIndex]);
            rightIndex++;
        }
    }
    return result.concat(left.slice(leftIndex).concat(right.slice(rightIndex)));
}
var sortedNumberArrayy = mergeSort([38, 27, 43, 10]);
var sortedStringArray = mergeSort(['JavaScript', 'GeeksforGeeks', 'TypeScript']);
console.log(sortedNumberArrayy);
console.log(sortedStringArray);

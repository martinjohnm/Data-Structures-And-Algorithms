



function mergeSort (arr : any[]) : any[]  {

    if (arr.length <= 1) {
        return arr
    }

    let middle = Math.floor(arr.length / 2)
    let leftArr = arr.slice(0,middle)
    let rightArr = arr.slice(middle)

    return mergeTwoSortedArray(mergeSort(leftArr), mergeSort(rightArr))

}




function mergeTwoSortedArray (left : any[], right : any[]) : any[] {

    let result : any[] = [];
    let leftIdx = 0;
    let rightIdx = 0;

    while (leftIdx < left.length && rightIdx < right.length) {


        if (left[leftIdx] < right[rightIdx]) {

            result.push( left[leftIdx] )
            leftIdx ++;
        } else {

            result.push( right[rightIdx] )
            rightIdx ++;
        }
    }

    return result.concat(left.slice(leftIdx).concat(right.slice(rightIdx)))

}


let sortedNumberArrayy: number[] =
    mergeSort([38, 27, 43, 10,5859, 5,5,5,5,5,4545,234,12,34,5,6,7,764325,3]);
console.log(sortedNumberArrayy);
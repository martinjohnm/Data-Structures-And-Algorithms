export async function bubbleSort(
    arr: number[],
    setArray: (arr: number[]) => void
  ) {
    const tempArr = [...arr];
    const len = tempArr.length;
    for (let i = 0; i < len - 1; i++) {
      for (let j = 0; j < len - i - 1; j++) {
        if (tempArr[j] > tempArr[j + 1]) {
          [tempArr[j], tempArr[j + 1]] = [tempArr[j + 1], tempArr[j]];
          setArray([...tempArr]);
          await new Promise((resolve) => setTimeout(resolve, 100)); // Delay for animation
        }
      }
    }
  }
  
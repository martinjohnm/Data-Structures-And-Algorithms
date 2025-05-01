import { motion } from "framer-motion";
import { useRecoilState } from "recoil";
import { bubbleSort } from "../algorithms/bubbleSort";
import { bubbleArrayState, isBubbleSorting } from "../store/atoms/bubbleSortState";

export const BubbleSortVisualizer = () => {
  const [array, setArray] = useRecoilState(bubbleArrayState);
  const [sorting, setSorting] = useRecoilState(isBubbleSorting);

  const generateArray = () => {
    setArray(Array.from({ length: 20 }, () => Math.floor(Math.random() * 100)));
  };

  const startSorting = async () => {
    setSorting(true);
    await bubbleSort(array, setArray);
    setSorting(false);
  };

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="flex gap-1">
        {array.map((value, idx) => (
          <motion.div
            key={idx}
            className="bg-blue-500 w-5"
            style={{ height: `${value * 3}px` }}
            animate={{ scale: sorting ? 1.1 : 1 }}
            transition={{ duration: 0.2 }}
          />
        ))}
      </div>
      <div className="flex gap-4">
        <button
          className="bg-green-500 text-white px-4 py-2 rounded"
          onClick={generateArray}
        >
          Generate
        </button>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded"
          onClick={startSorting}
          disabled={sorting}
        >
          Sort
        </button>
      </div>
    </div>
  );
};
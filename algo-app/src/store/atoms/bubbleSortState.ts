import { atom } from "recoil";

export const bubbleArrayState = atom<number[]>({
  key: "bubbleArrayState",
  default: [],
});

export const isBubbleSorting = atom<boolean>({
  key: "isBubbleSorting",
  default: false,
});

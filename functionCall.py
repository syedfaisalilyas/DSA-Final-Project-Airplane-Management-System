import SortingAlgorithm
import time


def SortingAlgorithmFunction_Call(A, sorttype, sortalgo):
    original = A.copy()
    res = []
    startTime = time.time()

    if sortalgo == "InsertionSort":
        res = SortingAlgorithm.InsertionSort(A, 0, len(A), sorttype)

    elif sortalgo == "SelectionSort":
        res = SortingAlgorithm.SelectionSort(A, sorttype)

    elif sortalgo == "MergeSort":
        res = SortingAlgorithm.merge_Sort(A, 0, len(A) - 1, sorttype)

    elif sortalgo == "BubbleSort":
        res = SortingAlgorithm.BubbleSort(A, sorttype)

    elif sortalgo == "QuickSort":
        res = SortingAlgorithm.quick_sort(A, sorttype)

    elif sortalgo == "HeapSort":
        res = SortingAlgorithm.HeapSort(A, len(A), sorttype)

    elif sortalgo == "CountingSort":
        res = SortingAlgorithm.merge_Sort(A, 0, len(A) - 1, sorttype)

    elif sortalgo == "RadixSort":
        res = SortingAlgorithm.HeapSort(A, len(A), sorttype)

    elif sortalgo == "BucketSort":
        # print("Enter...")
        res = SortingAlgorithm.merge_Sort(A, 0, len(A) - 1, sorttype)

    elif sortalgo == "CombSort":
        res = SortingAlgorithm.Combsort(A, sorttype)

    elif sortalgo == "ShellSort":
        res = SortingAlgorithm.ShellSort(A, sorttype)

    elif sortalgo == "CockailSort":
        res = SortingAlgorithm.CocktailSort(A, sorttype)

    elif sortalgo == "IndexSort":
        res = SortingAlgorithm.IndexSort(A, sorttype)

    elif sortalgo == "PancakeSort":
        res = SortingAlgorithm.PancakeSort(A, sorttype)


    endTime = time.time()
    totalTime = endTime - startTime
    return res, totalTime

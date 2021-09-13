import random
import time
from statistics import mean

from bubblesort import bubbleSort
from insertionsort import insertionSort
from mergesort import mergeSort
from quicksort import quickSort



def gemiddelde_case():
    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,10000), 1000)
        tic = time.perf_counter()
        bubbleSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"BubbleSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,10000), 1000)
        tic = time.perf_counter()
        insertionSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"InsertionSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,10000), 1000)
        tic = time.perf_counter()
        quickSort(lijst, 0, len(lijst)-1)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"QuickSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,10000), 1000)
        tic = time.perf_counter()
        mergeSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"MergeSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")


def worst_case():
    tijden = []
    lijst = [i for i in range(10000, 1, -1)]
    tic = time.perf_counter()
    bubbleSort(lijst)
    toc = time.perf_counter()
    tijden.append(toc-tic)

    print(f"BubbleSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")

    tijden = []
    lijst = [i for i in range(10000, 1, -1)]
    tic = time.perf_counter()
    insertionSort(lijst)
    toc = time.perf_counter()
    tijden.append(toc-tic)

    print(f"InsertionSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")

    tijden = []
    lijst = [i for i in range(10000, 1, -1)]
    tic = time.perf_counter()
    quickSort(lijst, 0, len(lijst)-1)
    toc = time.perf_counter()
    tijden.append(toc-tic)

    print(f"QuickSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")

    tijden = []
    lijst = [i for i in range(10000, 1, -1)]
    tic = time.perf_counter()
    mergeSort(lijst)
    toc = time.perf_counter()
    tijden.append(toc-tic)

    print(f"MergeSort deed gemiddeld {mean(tijden):0.8f} seconden over het sorteren van de lijst")


print("=================GEMIDDELDE CASE=================")
gemiddelde_case()
print("=================WORST CASE=================")
worst_case()
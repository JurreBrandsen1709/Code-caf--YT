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
        lijst = random.sample(range(1,100000), 10000)
        tic = time.perf_counter()
        bubbleSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"BubbleSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,100000), 10000)
        tic = time.perf_counter()
        insertionSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"InsertionSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,100000), 10000)
        tic = time.perf_counter()
        mergeSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"MergeSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        random.seed(1337)
        lijst = random.sample(range(1,100000), 10000)
        tic = time.perf_counter()
        quickSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"QuickSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

def worst_case():
    tijden = []
    for _ in range(0, 10):
        lijst = [i for i in range(10000, 1, -1)]
        tic = time.perf_counter()
        bubbleSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"BubbleSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        lijst = [i for i in range(10000, 1, -1)]
        tic = time.perf_counter()
        insertionSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"InsertionSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        lijst = [i for i in range(10000, 1, -1)]
        tic = time.perf_counter()
        mergeSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"MergeSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")

    tijden = []
    for _ in range(0, 10):
        lijst = [i for i in range(10000, 1, -1)]
        tic = time.perf_counter()
        quickSort(lijst)
        toc = time.perf_counter()
        tijden.append(toc-tic)

    print(f"QuickSort deed gemiddeld {mean(tijden):0.4f} seconden over het sorteren van de lijst")


worst_case()
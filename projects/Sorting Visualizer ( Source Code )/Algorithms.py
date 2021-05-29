from PyQt5 import QtTest


# Bubble Sort Algorithm
def BubbleSort(n, arr, drawData, speed):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            drawData([
                "blue" if x == j or x == j + 1 else "red" for x in range(n - i)
            ] + ["green"] * (i + 1))

            QtTest.QTest.qWait(speed * 1000)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            drawData(["red" for x in range(n - i)] + ["green"] * (i + 1))

            QtTest.QTest.qWait(speed * 1000)

    drawData(["green"] * n)
    QtTest.QTest.qWait(speed * 1000)


# Insertion Sort Algorithm
def InsertionSort(n, arr, drawData, speed):
    for i in range(1, n):
        j = i - 1
        x = arr[i]
        drawData(["green"] * j +
                 ["blue" if k == j or k == i else "red" for k in range(j, n)])

        QtTest.QTest.qWait(speed * 1000)
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            drawData(
                ["green"] * j +
                ["blue" if k == j or k == i else "red" for k in range(j, n)])

            QtTest.QTest.qWait(speed * 1000)
            j = j - 1
        arr[j + 1] = x
        drawData(["green"] * i + ["red" for k in range(i, n)])

        QtTest.QTest.qWait(speed * 1000)
    drawData(["green"] * n)
    QtTest.QTest.qWait(speed * 1000)


# Selection Sort Algorithm
def SelectionSort(n, arr, drawData, speed):
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            L = []
            for x in range(n):
                if x < i:
                    L.append("green")
                elif x == i:
                    L.append("violet")
                elif x == j:
                    L.append("blue")
                else:
                    L.append("red")
            drawData(L)

            QtTest.QTest.qWait(speed * 1000)
            if arr[j] < arr[k]:
                k = j
        L = []
        for x in range(n):
            if x < i:
                L.append("green")
            elif x == k:
                L.append("orange")
            else:
                L.append("red")
        drawData(L)

        QtTest.QTest.qWait(speed * 1000)
        arr[i], arr[k] = arr[k], arr[i]
    drawData(["green"] * n)


# Merge Sort Algorithm
def MergeSort(n, l, h, arr, drawData, speed):
    drawData(["orange" if x in range(l, h + 1) else "red" for x in range(n)])
    QtTest.QTest.qWait(speed * 1000)
    if l < h:
        mid = (l + h) // 2
        MergeSort(n, l, mid, arr, drawData, speed)
        MergeSort(n, mid + 1, h, arr, drawData, speed)
        Merge(n, l, mid, h, arr, drawData, speed)

    drawData(["green"] * n)


# Merges two Arrays
def Merge(n, l, mid, h, arr, drawData, speed):
    drawData(["orange" if x in range(l, h + 1) else "red" for x in range(n)])
    QtTest.QTest.qWait(speed * 1000)
    n1 = mid - l + 1
    n2 = h - mid

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        S = ["red"] * n
        for x in range(n):
            if x == i + l:
                S[i + l] = "violet"
            elif x == j + (mid + 1):
                S[j + (mid + 1)] = "blue"
        drawData(S)

        QtTest.QTest.qWait(speed * 1000)
        if L[i] <= R[j]:
            arr[k] = L[i]
            drawData(["red" for x in range(n)])

            QtTest.QTest.qWait(speed * 1000)
            i += 1
        else:
            arr[k] = R[j]
            drawData(["red" for x in range(n)])

            QtTest.QTest.qWait(speed * 1000)
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        drawData(["red" for x in range(n)])

        QtTest.QTest.qWait(speed * 1000)
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        drawData(["red" for x in range(n)])

        QtTest.QTest.qWait(speed * 1000)
        j += 1
        k += 1

    drawData(["green" if x in range(l, h + 1) else "red" for x in range(n)])
    QtTest.QTest.qWait(speed * 1000)


# Quick Sort Algorithm
def QuickSort(n, l, h, arr, drawData, speed):
    if l < h:
        p = Partition(l, h, arr, drawData, speed)
        QuickSort(n, l, p - 1, arr, drawData, speed)
        QuickSort(n, p + 1, h, arr, drawData, speed)
    drawData(["green"] * n)


def Partition(l, h, arr, drawData, speed):
    pivot_index = l
    pivot = arr[pivot_index]
    drawData(
        ["violet" if x == pivot_index else "red" for x in range(len(arr))])
    while l < h:
        while l < len(arr) and arr[l] <= pivot:
            R = []
            for x in range(len(arr)):
                if x == pivot_index:
                    R.append("violet")
                elif x == l:
                    R.append("blue")
                else:
                    R.append("red")
            drawData(R)

            QtTest.QTest.qWait(speed * 1000)
            l += 1

        while arr[h] > pivot:
            R = []
            for x in range(len(arr)):
                if x == pivot_index:
                    R.append("violet")
                elif x == h:
                    R.append("blue")
                else:
                    R.append("red")
            drawData(R)

            QtTest.QTest.qWait(speed * 1000)
            h -= 1

        if l < h:
            drawData([
                "blue" if x == h or x == l else "red" for x in range(len(arr))
            ])

            QtTest.QTest.qWait(speed * 1000)
            arr[l], arr[h] = arr[h], arr[l]
    drawData([
        "blue" if x == h or x == pivot_index else "red"
        for x in range(len(arr))
    ])
    QtTest.QTest.qWait(speed * 1000)
    arr[h], arr[pivot_index] = arr[pivot_index], arr[h]
    return h
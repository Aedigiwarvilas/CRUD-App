def Merge(l,mid,h,arr):
    i,j,k=l,mid+1,l
    temp = [0]*6
    # Copy data to temp arrays L[] and R[]
    while i <= mid and j <= h:

        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1


    # Checking if any element was left
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= h:
        temp[k] = arr[j]
        j += 1
        k += 1

    i=l
    while i<=h:
        arr[i]=temp[i]
        i+=1



# Merge Sort Algorithm
def MergeSort(l,h,arr):
    if l<h:
        mid = (l+h)//2
        MergeSort(l,mid,arr)
        MergeSort(mid+1,h,arr)
        Merge(l,mid,h,arr)

L=[1,6,2,5,3,4]
print("Before Applying Merge Sort")
print("The List is ")
print(L)
print("After Applying Merge Sort")
print("The List is ")
MergeSort(0,5,L)
print(L)

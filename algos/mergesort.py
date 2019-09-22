def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[0:mid]
        R=arr[mid:]
        print L, R
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        print arr

arr = [12, 11, 13, 5, 4, 44, 1]
mergesort(arr)
print arr

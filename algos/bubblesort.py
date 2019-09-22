arr = [56, 12, 11, 13, 5, 4, 44, 1] 
n=len(arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1]= arr[j+1], arr[j]
            print arr
print arr

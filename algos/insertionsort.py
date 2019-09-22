arr = [56, 12, 11, 13, 5, 4, 44, 1]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]: 
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    print arr
print arr

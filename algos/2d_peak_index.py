def findMax(arr, rows, mid): 
    maxx=0
    max_index = 0
    for i in range(rows): 
        if (maxx < arr[i][mid]): 
            maxx = arr[i][mid] 
            max_index = i 
    return maxx,max_index 
  
# Function to find a peak element 
def findPeakRec(arr, rows, columns, mid): 
    maxx, max_index = findMax(arr, rows, mid) 
    if mid==0 or mid==columns-1:
        return maxx
    if arr[max_index][mid]>=arr[max_index][mid+1] and arr[max_index][mid]>=arr[max_index][mid-1]:
        return maxx
    if arr[max_index][mid]<arr[max_index][mid+1]:
        if mid==mid+mid/2:
            mid=mid+1
        else:
            mid=mid+mid/2
        return findPeakRec(arr, rows, columns, mid)
    return findPeakRec(arr, rows, columns, mid-mid/2)

arr = [ [ 10, 8, 10], 
        [ 14, 13, 12], 
        [ 15, 9, 11], 
        [ 16, 17, 19] ]

rows = 4


columns = 3
midc=(columns-1)/2

x = findPeakRec(arr, rows, columns, midc)
print x

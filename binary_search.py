def bin_search(arr, left, high, key):
    left = 0
    high = len(arr)-1
    f=0
    ans = 0
    while(left<=high):
        mid = (left+high)//2
        if arr[mid] == key:
            f=1
            ans =mid
            break
        else:
            if key<arr[mid]:
                high = mid -1
            elif key>arr[mid]:
                left = mid+1
    if f==1:
        return mid
    else:
        return -1
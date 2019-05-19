while start<end:
	mid = (start+end)//2
	if arr[mid]>arr[mid+1]:
		return mid
	if arr[start]>arr[mid]:
		end = mid-1
	else:
		start= mid +1
return end
def bsearch(arr,start,end,k):
    f=0
    while(start<=end):
        mid= (start+end)//2
        if arr[mid]==k:
            f=1
            break
        else:
            if arr[mid]<k:
                start = mid+1
            elif arr[mid]>k:
                end = mid-1
    if f==1:
        print(mid)
    else:
        print(-1)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    pivot = findpivot(arr,0,n-1)
    if arr[pivot] == k:
        print(pivot)
    else:
        if k>=arr[0]:
            bsearch(arr,0,pivot-1,k)
        else:
            bsearch(arr,pivot+1,n-1,k)
        
            
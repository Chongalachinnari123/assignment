#prequires is list should be sorted.if not use sorting function 

def binarySearch(a,t,l):
     start = 0
     end = l-1
     while start <= end:
        mid = (start+end)//2 
        if t == a[mid]:

            return mid 
        elif t > a[mid]:
            start = mid + 1
        elif t < a[mid]:
            end = mid -1
     else:
        return("target not found")         
arr = [2,4,56,654,547,7657,585634,45346]
arr.sort()
t = 7657
l = len(arr)
print(binarySearch(arr,t,l))


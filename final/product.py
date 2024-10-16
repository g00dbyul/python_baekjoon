def product(candidate, n, arr):
    if len(candidate) == n:
        print(candidate)
        return
    for i in range(len(arr)):
        product(candidate+[arr[i]],n,arr)


product([],3,[1,2,3,4])
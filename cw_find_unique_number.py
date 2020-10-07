def find_uniq(arr):
    n = 0
    for i in range(len(arr)):
        if i == 0:
            if arr[i] != arr[i + 1] and arr[i] != arr[i + 2]:
                n = arr[i]
                break
        elif i == (len(arr) - 1):
            if arr[i] != arr[i - 1] and arr[i] != arr[i - 2]:
                n = arr[i]
                break
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                n = arr[i]
                break
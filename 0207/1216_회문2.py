def palindrome(arr, n):
    for i in range(len(arr)):
        for j in range(int(n/2)):
            if arr[i][j] != arr[i][n-j-1]:
                pass
            else:
                return len(arr)
        
    for j in range(len(arr)):



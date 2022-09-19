def countSwaps(a):
    # Write your code here
    count=0
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]= a[j+1],a[j]
                count=count+1        
        if count==0:
            break   
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    return a 
         
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

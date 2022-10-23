with open("iprb_test_2", "r") as f:
    val = f.read().split()
    [k, m, n] = [int(i) for i in val]

    denom = (k+m+n)*(k+m+n-1)/2
    num = (k+m+n)*(k+m+n-1)/2 - (m+n)*(m+n-1)/2 + 3/4 * m*(m-1)/2 + m*n/2
    print(num/denom)
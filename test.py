def ind_to_bin(i):
    if i == 0:
        return [0]

    if i % 2 == 0: arr = [ 0 for i in range(i//2+1) ]
    else: arr = [ 0 for i in range(i//2 + 1)]

    for b in range(len(arr)):
        arr[b] = int(i % (b+1) == 0)
    return arr

def to_bin(x):
    return int(bin(x)[2:])

def to_bin_arr(x):
    n = to_bin(x)
    return [int(i) for i in list(str(n))]

for i in range(10):
    print(to_bin_arr(i))
def ind_to_bin(x,tlen):
    n = to_bin(x)
    res = [int(i) for i in list(str(n))]
    while(len(res) < tlen):
        res = [0] + res
    return res

def to_bin(x):
    return int(bin(x)[2:])

traits_expansion = 4
tlen = 2
for i in range(traits_expansion):
    b = ind_to_bin(i,tlen)
    print("result",b)
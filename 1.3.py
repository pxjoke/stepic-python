in_n, in_k = map(int, input().split())


def C(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return C(n - 1, k) + C(n - 1, k - 1)


print(C(in_n, in_k))

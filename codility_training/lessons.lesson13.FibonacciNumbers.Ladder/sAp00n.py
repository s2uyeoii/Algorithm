def solution(A, B):
    # write your code in Python 3.6
    N = max(A) + 1
    fibo_list = getFibo(N)
    return [ fibo_list[A[idx]] % 2 ** B[idx] for idx in range(len(A)) ]


def getFibo(N):
    fibo_list = [1, 1]
    for i in range(2, N):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    return fibo_list

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
print(solution(A,B))

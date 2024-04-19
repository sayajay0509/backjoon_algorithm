TC = int(input())
for _ in range(TC):
    N = int(input())
    sj, si = map(int,input().split())
    lst =[]
    for _ in range(N):
        tj, ti = map(int,input().split())
        lst.append((ti,tj))
    ej, ei = map(int, input().split())
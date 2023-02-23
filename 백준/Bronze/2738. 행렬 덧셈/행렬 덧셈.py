n, m = map(int, input().split())

# read in matrix A
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# read in matrix B
b = []
for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

# compute the sum of A and B
c = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    c.append(row)

# print the resulting matrix
for row in c:
    print(' '.join(map(str, row)))
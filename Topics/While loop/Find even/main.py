n = int(input())
v = 1
while v in range(n):
    if not v % 2:
        print(v)
    v += 1

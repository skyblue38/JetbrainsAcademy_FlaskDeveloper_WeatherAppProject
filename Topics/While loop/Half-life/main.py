initial = int(input())
remaining = initial
final = int(input())
hl_count = 0
while final < remaining:
    hl_count += 1
    remaining = int(remaining / 2)
print(hl_count * 12)

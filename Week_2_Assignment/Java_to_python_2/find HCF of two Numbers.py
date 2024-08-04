n1, n2 = map(int, input("Enter two numbers: ").split())

while n1 != n2:
    if n1 > n2:
        n1 -= n2
    else:
        n2 -= n1

print(f"HCF: {n1}")

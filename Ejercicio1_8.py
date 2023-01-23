def to_decimal(n):
    list=[int(a) for a in str(n)]
    list.reverse()
    decimal = 0
    for i in range(len(list)):
        decimal = int(list[int(i)]) * 2 ** int(i)
    return decimal

def to_binary(n):
    binary=[]
    while n > 0:
        binary.append(str(n%2))
        n//=2
    binary.reverse()
    return ''.join(binary)

print(to_decimal(10010))
print(to_binary(14))
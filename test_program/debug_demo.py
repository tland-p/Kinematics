def sigma(n):
    z = 0
    for i in range(1, n+1):
        z = z + i
    return z


def main():
    n = int(input('n = '))
    result = sigma(n)
    print(result)


main()
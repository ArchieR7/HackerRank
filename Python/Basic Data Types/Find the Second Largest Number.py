if __name__ == '__main__':
    n = int(input())
    arr = set([int(x) for x in input().split()])
    arr.remove(max(arr))
    print(max(arr))
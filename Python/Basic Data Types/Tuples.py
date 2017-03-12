if __name__ == '__main__':
    n = int(input())
    t = ()
    integer_list = map(int, input().split())
    for i in integer_list:
        t += (i,)
    print(hash(t))
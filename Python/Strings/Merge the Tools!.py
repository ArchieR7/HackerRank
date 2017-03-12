def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,round(len(string)/k)):
        s = string[k * i:k * (i + 1)]
        ss = []
        a = ''
        for i in s:
            if i in ss:
                continue
            else :
                a += i
                ss.append(i)
        print(a)
   
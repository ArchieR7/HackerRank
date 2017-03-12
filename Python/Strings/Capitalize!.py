def capitalize(string):
    new = ''
    for i in range(0,len(string)):
        if i == 0:
            new += string[i].upper()
        elif string[i - 1] == ' ':
            new += string[i].upper()
        else :
            new += string[i]
    return new
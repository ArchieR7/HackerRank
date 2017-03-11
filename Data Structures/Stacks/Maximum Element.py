class Archie:
    def __init__(self, value, index):
        self.value = value
        self.index = index

commands = []

for _ in range(int(input())):
    commands.append(input().split())
    
queue = []
a= Archie(0, 0)
for command in commands:
    c = command[0]
    if c == '1':
        queue.append(int(command[1]))
        if int(command[1]) > a.value:
            a.value = int(command[1])
            a.index = len(queue) - 1
    elif c == '2':
        queue.pop(len(queue) - 1)
        if a.index == len(queue):
            if len(queue) > 0:
                m = max(queue)
                a.value = m
                i = queue.index(m)
                a.index = i
            else :
                a.index = 0
                a.value = 0
    else :
        print(a.value)
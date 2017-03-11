import sys

class Node:
	def __init__(self, value):
		self.degree = 1
		self.value = value
		self.top = None
		self.left = None
		self.right = None
		self.is_enabled = True

	def set_top(self, top):
		self.top = top
		self.degree = top.degree + 1

		if top.left is None:
			top.left = self
		else :
			top.right = self

def check_none(n):
	return n.left is None or n.right is None


initial_node = Node(1)

N = int(input())
nodes = [initial_node]

while sum(1 for x in nodes if check_none(x)) > 0:
	target = [x for x in nodes if check_none(x)][0]
	numbers = [int(x) for x in input().split()]
	if numbers[0] == -1:
		target.left = -1
	else :
		left = Node(numbers[0])
		left.set_top(target)
		nodes.append(left)
	if numbers[1] == -1:
		target.right = -1
	else :
		right = Node(numbers[1])
		right.set_top(target)
		nodes.append(right)

S_count = int(input())
l = []
for i in range(0,S_count):
	l.append(int(input()))
for i in l:
    for x in nodes:
        if x.degree % i == 0:
            # print('swap {x}'.format(x=x.value))
            temp = x.left
            x.left = x.right
            x.right = temp
        x.is_enabled = True
    current_node = initial_node
    ans = []
    while len(ans) < N:
        # print('{c}->'.format(c=current_node.value))
        if current_node.left != -1 and current_node.left.is_enabled:
            current_node = current_node.left
        else :
            ans.append(current_node.value)
            current_node.is_enabled = False
            if current_node.right != -1:
                current_node = current_node.right
                # print('Select right.')
            else :
                # print('Back to top.')
                if current_node.top != None:
	                current_node = current_node.top
                else :
                	break
                while current_node.is_enabled == False:
                    if current_node.top != None:
                        current_node = current_node.top
                    else :
                        break
    print(' '.join(str(a) for a in ans))
class Solution:
    def __init__(self):
        self.string1 = []
        self.string2 = []
    # Write your code here
    def pushCharacter(self, c):
        self.string1.append(c)
    def enqueueCharacter(self, c):
        self.string2.append(c)
    def popCharacter(self):
        return self.string1.pop()
    def dequeueCharacter(self):
        r = self.string2[0]
        self.string2.remove(r)
        return r
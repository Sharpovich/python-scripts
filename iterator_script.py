from random import random

class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
                self.i += 1
                return random()
        else:
            raise StopIteration

for i in RandomIterator(10):
    print(i)

    
    x=[-2,-1,0,1,2]
y=[]
for i in x:
    y.append(i*i)
print(y)

x=[-2,-1,0,1,2]
y=[i*i for i in x if i>0]
print(y)

z=[(x,y) for x in range(3) for y in range(3) if y>=x]
print(z)

z=[]
for x in range(3):
    for y in range(3):
        if y>=x:
            z.append((x,y))
print(z)

a = [i + 1 for i in range(4)]
print(a)
a = [i for i in range(4)]
print(a)
a = [i for i in range(5)][1:]
print(a)
a = list(i + 1 for i in range(4))
print(a)

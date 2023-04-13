import random

x = random.randint(0, 10)
print(x)

def more_or_less(num):
    if x >= 5:
        print('more')
    else:
        print('less')

more_or_less(x)

y = 0

while y < 10:
    print(y)
    y += 1
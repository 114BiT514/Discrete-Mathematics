num = int(raw_input())
k = 1
a = num
while a != 0:
    a = (a + num)%18
    k += 1
print k
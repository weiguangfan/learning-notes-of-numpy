a = [i for i in range(10)]
b = [i for i in range(10)]
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
print(c)
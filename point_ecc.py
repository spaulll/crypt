def point_gen(a, b, m):
    y = []
    x = []
    points = []
    for i in range(m):
        y.append((i ** 2) % m)
        x.append(((i ** 3 + (a * i) + b )) % m) 

    # print(y)
    # print(x)

    for i in range(m):
        for j in range(m):
            if x[i] == y[j]:
                points.append((i,j))
    return points
m = int(input("Enter the modulas: "))
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

points = point_gen(a, b, m)
print(f"Points are: {points}")
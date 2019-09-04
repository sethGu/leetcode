i = input().split()
x, y, s = [abs(int(each)) for each in i]

if s < x + y:
    print("No")
else:
    if (s - x - y) % 2 == 0:
        print("Yes")
    else:
        print("No")

a = []
b = []
sum = 0
max = 0
n = int(input())  # 第一行的输入n个站点
for i in range(n):
    p, q = list(map(int, input().split()))  # 往后若干行
    a.append(p)
    b.append(q)

for i in range(n):
    sum -= a[i] + b[i]
    if sum[i] > max: max = sum[i]

print(max)

# !/usr/bin/python3
a = []  # 下车队列
b = []  # 上车队列
t = 0  # 车上人数
t_max = 0  # 最大车上人数
n = int(input())

for i in range(n):
    p, q = list(map(int, input().split()))
    a.append(p)
    b.append(q)

for i in range(n):
    t += b[i] - a[i]
    if t > t_max:
        t_max = t

print(t_max)

while 1:
    n = int(input())
    for i in range(n):
        str = input()
        out = ''
        for j in str:
            if j == "#":
                out = out[:-1]
            elif j == "@":
                out = ''
            else:
                out += j
    print(out)

############################################################

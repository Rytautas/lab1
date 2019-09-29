import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    a = (x**2 - 7)**2 - 1
    return a


fi = 0
i = 0
l = 0
r = 10
e = 0.0001

t = (math.sqrt(5) - 1) / 2
list3 = np.array([])

x = np.linspace(0, 10, 100)
temp = (x**2 - 7)**2 - 1
fig1, ax = plt.subplots()
plt.axvline(linewidth=2, color='black')
plt.axhline(linewidth=2, color='black')
ax.set_ylabel('f(x)')
ax.set_xlabel('x')
plt.grid(axis='both')
ax.plot(x, temp)

# region zoom
x = np.linspace(0, 5, 100)
temp = (x**2 - 7)**2 - 1
fig2, ax = plt.subplots()
plt.axvline(linewidth=2, color='black')
plt.axhline(linewidth=2, color='black')
ax.set_ylabel('f(x)')
ax.set_xlabel('x')
plt.grid(axis='both')
ax.plot(x, temp)
# endregion

x1 = r - ((r - l) * t)
x2 = l + ((r - l) * t)

plt.axvline(x=x1, linestyle='--', linewidth=0.25, color="black")
plt.axvline(x=x2, linestyle='--', linewidth=0.25, color="black")

while (r - l) > e:
    i += 1

    if f(x2) < f(x1):
        fi += 2
        l = x1
        x1 = x2
        x2 = l + ((r - l) * t)
        plt.axvline(x=x2, linestyle='--', linewidth=0.25, color="black")
        list3 = np.append(list3, x2)
    else:
        fi += 2
        r = x2
        x2 = x1
        x1 = r - ((r - l) * t)
        plt.axvline(x=x1, linestyle='--', linewidth=0.25, color="black")
        list3 = np.append(list3, x1)

wr = open("result2.txt", "w+")
wr.write("Atliktu zingsniu skaicius: %d\r\n" % i)
wr.write("Atliktu funkcijos skaiciavimu skaicius: %d\r\n" % fi)
wr.write("Bandymo taskai:\n")
wr.write("step        x               f(x):\n")
j = 0
for a in list3:
    wr.write("%d.      %.9f        %.9f\n" % (j+1, a, f(a)))
    j += 1
wr.close()

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    a = (x**2 - 7)**2 - 1
    return a


fi = 0
l = 0
r = 10
e = 0.0001
xm = (l + r) / 2
i = 0

listxm = np.array([])

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

while (r - l) > e:
    i += 1
    x1 = l + ((r - l) / 4)
    x2 = r - ((r - l) / 4)

    listxm = np.append(listxm, xm)

    # plt.axvline(x=x1, linestyle='--', linewidth=0.25, color="black")
    # plt.axvline(x=x2, linestyle='--', linewidth=0.25, color="black")
    plt.axvline(x=xm, linestyle='--', linewidth=0.25, color="black")

    if f(x1) < f(xm):
        fi += 2
        r = xm
        xm = x1
    else:
        if f(x2) < f(xm):
            fi += 4
            l = xm
            xm = x2
        else:
            fi += 4
            l = x1
            r = x2

wr = open("result1.txt", "w+")
wr.write("Atliktu zingsniu skaicius: %d\r\n" % i)
wr.write("Atliktu funkcijos skaiciavimu skaicius: %d\r\n" % fi)
wr.write("Bandymo taskai:\n")
wr.write("step        x               f(x):\n")
j = 0
for a in listxm:
    wr.write("%d.      %.9f        %.9f\n" % (j+1, a, f(a)))
    j += 1
wr.close()

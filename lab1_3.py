import numpy as np
import matplotlib.pyplot as plt
import math as m


def f(a):
    return (a**2 - 7)**2 - 1


def deriv(a):
    return 4 * a * (a**2 - 7)


fi = 0
i = 0
e = 0.0001
x0 = 5
list = np.array([x0])
h = x0


x = np.linspace(0, 10, 100)
tempf = (x**2 - 7)**2 - 1
tempd = 4 * x * (x**2 - 7)
fig1, ax = plt.subplots()
ax.plot(x, tempf)
ax.plot(x, tempd)
labels = ['f(x)', 'f\'(x)']
plt.legend(labels)
plt.axvline(linewidth=2, color='black')
plt.axhline(linewidth=2, color='black')
ax.set_xlabel('x')
plt.grid(axis='both')


# region zoom
x = np.linspace(0, 5, 100)
tempf = (x**2 - 7)**2 - 1
tempd = 4 * x * (x**2 - 7)
fig2, ax = plt.subplots()
ax.plot(x, tempf)
ax.plot(x, tempd)
labels = ['f(x)', 'f\'(x)']
plt.legend(labels)
plt.axvline(linewidth=2, color='black')
plt.axhline(linewidth=2, color='black')
ax.set_xlabel('x')
plt.grid(axis='both')
# endregion

while m.fabs(h) > e:
    i += 1

    plt.axvline(x=x0, linestyle='--', linewidth=0.25, color="r")
    h = f(x0)/deriv(x0)
    x1 = x0 - h

    fi += 2
    list = np.append(list, x1)
    x0 = x1

wr = open("result3.txt", "w+")
wr.write("Atliktu zingsniu skaicius: %d\r\n" % i)
wr.write("Atliktu funkcijos skaiciavimu skaicius: %d\r\n" % fi)
wr.write("Bandymo taskai:\n")
wr.write("step        x               f(x):\n")
j = 0
for a in list:
    wr.write("%d.      %.9f        %.9f\n" % (j, a, f(a)))
    j += 1
wr.close()

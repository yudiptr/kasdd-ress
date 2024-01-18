w0 = 1
w1 = 1

x1 = 0
y1 = 0
x2 = 1
y2 = 2
x3 = 2
y3 = 7

a = 0.1

max_iter = 1000
while max_iter != 0:
    w0_temp = 1/2 * 2 * ((w0 + w1*x1 - y1) +
                         (w0 + w1*x2 - y2) + (w0 + w1*x3 - y3))
    w1_temp = 1/2 * 2 * (x1*(w0 + w1*x1 - y1) + x2 *
                         (w0 + w1*x2 - y2) + x3*(w0 + w1*x3 - y3))

    w0 = w0 - a * w0_temp
    w1 = w1 - a * w1_temp

    max_iter -= 1

print(w0)
print(w1)
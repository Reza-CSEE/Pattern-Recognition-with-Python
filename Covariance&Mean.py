import numpy as np
# x = str(input("please enter all X:"))
# y = str(input("please enter all Y:"))
x1 = [0, 1,  2, 3, 4, 5]
y1 = [0, 1,  2, 2, 2, 3]
print("Covariance of W1 is:\n", np.cov(x1, y1))
print("Mean of W1 is:\n", [np.mean(x1), np.mean(y1)])

x2 = [6, 8,  9, 9, 10, 11, 12, 12]
y2 = [9, 10,  10, 11, 10, 12, 12, 13]
print("Covariance of W2 is:\n", np.cov(x2, y2))
print("Mean of W2 is:\n", [np.mean(x2), np.mean(y2)])

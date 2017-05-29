import numpy
e = 0.00001

arr = numpy.array([[6.7, 1.1, 0.97, 1.18, -0.36],
                  [1.1, 3.72, 1.3, -1.63, -0.33],
                  [0.97, -2.46, 5.88, 2.1, 0.133],
                  [1.3, 0.16, 2.1, 5.66, 0.],
                  [0.84, -0.33, 0.133, 0., 4.]])
b = numpy.array([2.1, 0.48, 0., 3.68, -0.48])
X = numpy.array([1., 1., 0., 1., -1.])
n, m = arr.shape
temp = numpy.zeros(n)
count = 0
normarr = numpy.ones(n)
while numpy.linalg.norm(normarr) > e:
    for i in range(0, n, 1):
        temp[i] = b[i]
        for g in range(0, n, 1):
            if i != g:
                temp[i] -= arr[i, g] * X[g]
        temp[i] /= arr[i, i]
    for h in range(0, n, 1):
        normarr[h] = abs(X[h] - temp[h])
        X[h] = temp[h]
    count += 1
    print count, ' iteration\nvec reshenii:', X, '\nvector normy:', normarr, '\nnorma: ', numpy.linalg.norm(normarr), '\n'

''''{:F}'.format(numpy.linalg.norm(normarr))'''
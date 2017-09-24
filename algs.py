def euler(X, y0, h, f):

    Y = [y0]
    for i in range(1, len(X)):
        yi = Y[i - 1] + h * f(X[i - 1], Y[i - 1])
        Y.append(yi)

    dY = get_dY(X, Y, h, f)

    return Y, dY

def get_dY(X, Y, h, f):

    dY = []
    for i in range(0, len(X)):
        dy = h * f(X[i], Y[i])
        dY.append(dy)

    return dY

def euler_cauchy(X, y0, h, f):

    Y = [y0]
    for i in range(1, len(X)):
        y_t = Y[i - 1] + h * f(X[i - 1], Y[i - 1])
        y = Y[i - 1] + h * ( f(X[i - 1], Y[i - 1]) + f(X[i], y_t)) / 2
        Y.append(y)

    dY = get_dY(X, Y, h, f)

    return Y, dY

def runge_kutta(X, y0, h, f):

    Y = [y0]
    for i in range(len(X) - 1):
        K1_i = h * f(X[i], Y[i])
        K2_i = h * f(X[i] + h / 2, Y[i] + K1_i / 2)
        K3_i = h * f(X[i] + h / 2, Y[i] + K2_i / 2)
        K4_i = h * f(X[i] + h, Y[i] + K3_i)
        dy = (K1_i + 2 * K2_i + 2 * K3_i + K4_i) / 6
        y_next = Y[i] + dy
        Y.append(y_next)

    return Y

def adams(X, y0, h, f):

    Y = runge_kutta(X, y0, h, f)
    for i in range(4, len(X)):

        _ = 55 * f(X[i - 1], Y[i - 1]) - 59 * f(X[i - 2], Y[i - 2])\
             + 37 * f(X[i - 3], Y[i - 3]) - 9 * f(X[i - 4], Y[i - 4])

        yi = Y[i - 1] + h * _ / 24

        Y[i] = yi

    return Y



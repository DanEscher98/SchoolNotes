import csv
import pandas as pd
import matplotlib.pyplot as plt
import rand_functions


def gradient_descent(m_now, b_now, points, l):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].x
        y = points.iloc[i].y
        m_gradient += -(2/n) * (y - (m_now * x + b_now)) * x
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * l
    b = b_now - b_gradient * l
    return m, b


## Main Program
if __name__=='__main__':
    lower_b = -200
    upper_b = 200
    
    rand_f = rand_functions.three_a
    filename = 'data.csv'
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['x', 'y'])
        for i in range(lower_b, upper_b):
            csvwriter.writerow([i, rand_f(i)])

    m = 0
    b = 0
    l = 0.000001
    epochs = 250
    data = pd.read_csv(filename)

    for i in range(epochs):
        if i % 50 == 0:
            print(f"Epoch: {i}")
        m, b = gradient_descent(m, b, data, l)

    plt.scatter(data.x, data.y, s=5, color="black")
    plt.plot(list(range(lower_b, upper_b)),
             [m * x + b for x in range(lower_b, upper_b)],
             color="red" )
    plt.show()

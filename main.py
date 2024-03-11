import numpy as np
import matplotlib.pyplot as plt


def plot_graph(equation, x_range=(-10, 10), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = eval(equation)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of ' + equation)
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to Python Graphing Calculator!")
    print("Enter your equation in terms of 'x', e.g., 'x**2 + 2*x - 3'")
    equation = input("Enter equation: ")
    x_min = float(input("Enter minimum x value: "))
    x_max = float(input("Enter maximum x value: "))
    num_points = int(input("Enter number of points to plot: "))

    plot_graph(equation, x_range=(x_min, x_max), num_points=num_points)

if __name__ == "__main__":
    main()

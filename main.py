#   proof of concept grafritare, (gjord med ai).
import numpy as np
import matplotlib.pyplot as plt
# importerar libraries

def plot_graph(equation, x_range=(-10, 10), num_points=1000):
    # funktion som ritar graf för gedd ekvation
    x = np.linspace(x_range[0], x_range[1], num_points)     # skapar fördelade x-värden
    y = eval(equation)  # utvärderar ekvationen tar x och sätter respektive y värde

    plt.plot(x, y)  # plottar x o y
    plt.xlabel('x')
    plt.ylabel('y')
        # sätter "label" på x o y
    plt.title('Graph of ' + equation)
        # titel på grafen
    plt.grid(True) # visar rutnät på grafritaren
    plt.show()

def main():
    print("Welcome to Python Graphing Calculator!")
    print("Enter your equation in terms of 'x', e.g., 'x**2 + 2*x - 3'")
    equation = input("Enter equation: ")
    x_min = float(input("Enter minimum x value: "))
    x_max = float(input("Enter maximum x value: "))
    num_points = int(input("Enter number of points to plot: "))
    # användarinput och instruktioner

    plot_graph(equation, x_range=(x_min, x_max), num_points=num_points)
        # ritar grafen med användarinput

if __name__ == "__main__":
    main()

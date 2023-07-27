import scipy.special
import numpy as np
from tkinter import *

width, height = 800, 600  # Define your variables

# Function to calculate a Bézier curve from control points.
def calculate_bezier_curve(control_points, num_points=1000):
    n = len(control_points)
    b = [scipy.special.comb(n - 1, i) for i in range(n)]
    r = np.arange(num_points) / (num_points - 1)
    bezier_curve = np.zeros((num_points, 2))
    for i in range(n):
        p = np.array([[(1 - t) ** (n - 1 - i) * t ** i for t in r]]).T
        bezier_curve += p * b[i] * control_points[i]
    return bezier_curve

# Function to calculate the derivative of a Bézier curve.
def calculate_derivative(control_points, num_points=1000):
    n = len(control_points)
    b = [scipy.special.comb(n - 2, i) * (n - 1) for i in range(n - 1)]
    r = np.arange(num_points) / (num_points - 1)
    derivative = np.zeros((num_points, 2))
    for i in range(n - 1):
        p = np.array([[(1 - t) ** (n - 2 - i) * t ** i for t in r]]).T
        derivative += p * b[i] * (control_points[i + 1] - control_points[i])
    return derivative

def calculate_acceleration(velocity, num_points=1000):
    n = len(velocity)
    b = [scipy.special.comb(n - 2, i) * (n - 1) for i in range(n - 1)]
    r = np.arange(num_points) / (num_points - 1)
    acceleration = np.zeros((num_points, 2))
    for i in range(n - 1):
        p = np.array([[(1 - t) ** (n - 2 - i) * t ** i for t in r]]).T
        acceleration += p * b[i] * (velocity[i + 1] - velocity[i])
    return acceleration

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.control_points = []
        


    def create_widgets(self):
        self.canvas = Canvas(self, width=width, height=height)  # Use variables for the Canvas size
        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.pack()

        

        self.clear_button = Button(self)
        self.clear_button["text"] = "Clear"
        self.clear_button["command"] = self.clear_canvas
        self.clear_button.pack()

    def add_point(self, event):
        x, y = event.x, event.y
        self.control_points.append(np.array([x, y]))
        self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black")

        if len(self.control_points) > 1:
            self.draw_curve()

    def draw_curve(self):
        self.canvas.delete("curve")
        curve = calculate_bezier_curve(self.control_points)
        for i in range(len(curve) - 1):
            self.canvas.create_line(*curve[i], *curve[i + 1], fill="blue", tags="curve")
        self.draw_vectors(curve)

    def draw_vectors(self, curve):
        velocity = calculate_derivative(self.control_points)
        acceleration = calculate_acceleration(velocity)
        for i in range(0, len(curve), 50):  # Only plotting every 50th vector for clarity
            self.canvas.create_line(*curve[i], *(curve[i] + velocity[i]/25), fill="red", tags="curve")  # Scaling down for visibility
            self.canvas.create_line(*curve[i], *(curve[i] + acceleration[i]/50), fill="green", tags="curve")  # Scaling down for visibility

    def clear_canvas(self):
        self.canvas.delete("all")
        self.control_points = []


root = Tk()
root.geometry(f"{width}x{height}")  # Use variables in the geometry
app = Application(master=root)
app.mainloop()


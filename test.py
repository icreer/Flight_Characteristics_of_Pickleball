from numpy import pi, cos, sin, sqrt,array
import matplotlib.pyplot as plt
import pandas as pd

types = 40
data = pd.read_csv("Drag_Data_Final.csv")
data = data[f"Total_{types}"]

print(data[1])
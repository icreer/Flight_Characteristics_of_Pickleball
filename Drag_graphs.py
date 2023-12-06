import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Drag_Data_Final.csv")
print(data.head())

data = data.drop([0,1,2])
Air = data["Air Speed"]


total0 = data["Total_0"] 
friction0 = data["Friction_0"]
rho0 = data["Rho_0"]

total26 = data["Total_26"] 
friction26 = data["Friction_26"]
rho26 = data["Rho_26"]

total40= data["Total_40"] 
friction40= data["Friction_40"]
rho40 = data["Rho_40"]


plt.subplot()

plt.title("Coeffiecent of Drag for Zero Hole ball ")
plt.xlabel("Air Speed (m/s)")
plt.ylabel("Drag Coeffiecent")

plt.scatter(Air,total0, marker="X", label = "Total")
plt.scatter(Air, friction0, marker="*", label="Friction")
plt.scatter(Air,rho0,marker = "^", label ="Pressure")
plt.legend(loc="upper right", title = "Type of Drag Coeffenct")

plt.show()

plt.subplot()

plt.title("Coeffiecent of Drag for 26 Hole ball ")
plt.xlabel("Air Speed (m/s)")
plt.ylabel("Drag Coeffiecent")

plt.scatter(Air,total26, marker="X", label = "Total")
plt.scatter(Air, friction26, marker="*", label="Friction")
plt.scatter(Air,rho26,marker = "^", label ="Pressure")
plt.legend(loc="upper right", title = "Type of Drag Coeffenct")

plt.show()

plt.subplot()

plt.title("Coeffiecent of Drag for 40 Hole ball ")
plt.xlabel("Air Speed (m/s)")
plt.ylabel("Drag Coeffiecent")

plt.scatter(Air,total40, marker="X", label = "Total")
plt.scatter(Air, friction40, marker="*", label="Friction")
plt.scatter(Air,rho40,marker = "^", label ="Pressure")
plt.legend(loc="upper right", title = "Type of Drag Coeffenct")

plt.show()

plt.title("Coeffiecent of Drag Depend on Air Friction")
plt.xlabel("Air Speed (m/s)")
plt.ylabel("Drag Coeffiecent")

plt.scatter(Air,friction0, marker="X", label = "0")
plt.scatter(Air, friction26, marker="*", label="26")
plt.scatter(Air,friction40,marker = "^", label ="40")
plt.legend(loc="upper right", title = "Number of Holes")

plt.show()

plt.title("Coeffiecent of Drag Depend on Air Pressure")
plt.xlabel("Air Speed (m/s)")
plt.ylabel("Drag Coeffiecent")

plt.scatter(Air,rho0, marker="X", label = "0")
plt.scatter(Air, rho26, marker="*", label="26")
plt.scatter(Air,rho40,marker = "^", label ="40")
plt.legend(loc="upper right", title = "Number of Holes")

plt.show()

plt.subplot()

plt.title("Total Coeffiecent of Drag")
plt.xlabel("Air Speed (m/s)")
plt.ylabel("Drag Coeffiecent")

plt.scatter(Air,total0, marker="X", label = "0")
plt.scatter(Air, total26, marker="*", label="26")
plt.scatter(Air,total40,marker = "^", label ="40")
plt.legend(loc="upper right", title = "Number of Holes")

plt.show()
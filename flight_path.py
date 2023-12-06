from numpy import pi, cos, sin, sqrt,array
import matplotlib.pyplot as plt
import pandas as pd


def flight_path(types,d):

    def total_speed(v):
        return sqrt((v[x])**2 + v[y]**2 + v[z]**2)

    def drag(v, types):
        data = pd.read_csv("Drag_Data_Final.csv")
        data = data[f"Total_{types}"]
        v += 5
        v = int(v)
        return data[v]
    v0 = 20 # m/s
    angle = 45 * pi / 180 # 9 degrees but needs to be converd to radians

    g = 9.8 # m/s^2

    dt = 0.01 # s

    # this is the index number that is assigned the list
    x = 0
    y = 1
    z = 2

    p = 1.00 # kg/m^2
    m = 0.02651 # kg 26.51g
    d = 0.0730# meter

    w =[0,d*2000 * 2* pi / 60,0] # Angluar speed
    v = [v0*cos(angle), v0*sin(angle), 0]
    V = [v0]
    a = [0,0,0]
    location = [[0],[0.5],[0]]

    A = pi * (d/2)**2
    t = 0 #s 
    while location[y][-1] > 0:

        V.append(total_speed(v)) # Keeping track of the total speed

        # This is due to the speed of the ball
        C = drag(total_speed(v),types)

        # Find the acceration in all direction
        a[x] = (-1 *C *A * p * v[x] * v[x])/m  + (.25/abs(w[y])) * w[y] * v[z]

        if abs(v[y]) == v[y]:
            a[y] = (-1 *C *A * p * v[y] * v[y])/m - g
        else:
            a[y] = (1 *C *A * p * v[y] * v[y])/m - g

        if abs(v[z]) == v[z]:
            a[z] = (-1 * C * A * p * v[z] * v[z])/m  + (.25/abs(w[y])) * w[y] * v[x]
        else:
            a[z] = ( C * A * p * v[z] * v[z])/m  + (.25/abs(w[y])) * v[x] * w[y]

        # Euler Methiod
        v[x] += a[x] * dt
        v[y] += a[y] * dt
        v[z] += a[z] * dt

        xl = location[x][-1] + v[x] *dt
        location[x].append(xl)


        yl = location[y][-1] + v[y] *dt
        location[y].append(yl)


        zl = location[z][-1] + v[z] *dt
        location[z].append(zl)
        t += dt
    # Creating simple list
    x_list = location[x]
    y_list = location[y]
    z_list = location[z]

    fig = plt.figure(figsize = (5,5))
    ax = plt.axes(projection = '3d')
    #ax.axes(projection = '3d') # Creates teh projection that the image needs
    #plt.title(f"Flight path of {types} Hole Ball with Flight time of {t}")

    ax.scatter3D(x_list,z_list,y_list,'r-') # Creates a 3D Scatter plot with x,y,z
    ax.set_xlabel("X (Meter)")
    ax.set_ylabel("z (Meter)")
    ax.set_zlabel("y (Meter)")
    plt.title(f"Flight path of {types} Hole Ball with Flight time of {round(t,2)} seconds")
    plt.show()

flight_path(0,-1)
flight_path(26,-1)
flight_path(40,-1)
flight_path(0,1)
flight_path(26,1)
flight_path(40,1)
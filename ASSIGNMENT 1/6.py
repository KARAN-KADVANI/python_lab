import math
x=[]
y=[]
z=[]

for i in range(0,10,1):

    x.append(input(f"enter the x coordinate of point {i+1} : "))
    y.append(input(f"enter the y coordinate of point {i+1} : "))
    z.append(input(f"enter the z coordinate of point {i+1} : "))

for i in range(0,10,1):
    for j in range(i+1,10,1):
        distance=math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2  +  (z[i]-z[j])**2)
        if distance <=minimum:
            minimum=distance
            nearest_neighbour=


    

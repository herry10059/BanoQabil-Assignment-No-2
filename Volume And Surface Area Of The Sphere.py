# Write a program that prompts the user to enter a radius and then calculates the volume and surface area of sphere.

radius= float(input("Enter the radius of sphere"))
volume=(4/3)*3.142*(pow(radius,3))
print ("The volume of sphere is %f" %volume)
s_area= 4*3.142*(pow(radius,2))
print ("The surface area of sphere %f" %s_area)

# Challenge
# Do a program that to ask the radio and calculate the area.
# author G.Seidel
# date 11/14/2022

import math # the math was used for get the Pi value. 
radio = (input("type a radio about the circle: "))

# area cicle is pi*radio^2
pi = math.pi
area = pi*float(radio)**2
print("The area about the circle is: ", area)
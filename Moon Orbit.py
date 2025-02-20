import matplotlib.pyplot as plt
import numpy as np
from astropy.time import TimeDelta

#Constants
G = 6.67430e-11
#Earth parameters
M_earth = 	5.97217e24 #kg
#Moon parameters
M_moon = 7.346e22 #kg
R_moon = 1737400 #m
a_moon = 384399000 #m
b_moon = a_moon * np.sqrt(1 - e_moon ** 2)
e_moon = 0.0549
#Velocity of moon
mu = G * (M_earth + M_moon)
v_moon = np.sqrt(mu  / a_moon) / 1000
print(f'Velocity of moon = ', v_moon , 'km/s')

#Orbital period of moon
T_sec = 2 * np.pi * np.sqrt((a_moon ** 3) / mu)

# Create a TimeDelta object
td = TimeDelta(T_sec, format='sec')
# Convert to days, hours, minutes, and seconds
total_days = td.to_value("day")
days, rem_hours = divmod(total_days * 24, 24)
hours, rem_minutes = divmod(rem_hours * 60, 60)
minutes, seconds = divmod(rem_minutes * 60, 60)
print(f"Orbital period: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds")

#Calculate Apogee and Perigee
pe_moon = (a_moon * (1 - e_moon)) / 1000
ap_moon = (a_moon * (1 + e_moon))/ 1000
print(f'Perigee of moon: {pe_moon} km')
print(f'Apogee of moon: {ap_moon} km')


# Compute the center of the ellipse (Moon's orbit is offset from Earth)
focus_distance = a_moon * e_moon  # Distance from center to focus
center_x = -focus_distance  # Earth is at one of the foci

#Generate points for plot
vu = np.linspace(0, 2 * np.pi, 1000)
x = a_moon * np.cos(vu)
y = b_moon * np.sin(vu)

# Shift the ellipse so Earth is at one focus
x_shifted = x + center_x
#plot
plt.figure(figsize=(8, 6))
plt.plot(x_shifted, y, label="Moon's Orbit", color='red')
plt.scatter(0, 0, color='blue', s=100, label='Earth')  # Earth at the origin

# Labels and formatting
plt.xlabel("Distance (m)")
plt.ylabel("Distance (m)")
plt.title("Moon's Orbit Around Earth")
plt.axis("equal")
plt.legend()
plt.grid()
plt.show()

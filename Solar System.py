import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')  # Apply a dark theme

center = (0, 0)

# planetary_parameters = {
#     'Mercury': {'a': 5.791e7 / M_TO_AU, 'e': 0.205630, 'true_anomaly': 67.560108},
#     'Venus': {'a': 1.0821e8 / M_TO_AU, 'e': 0.006772, 'true_anomaly': 181.97909950},
#     'Earth': {'a': 1.49598023e8 / M_TO_AU, 'e': 0.0167086, 'true_anomaly': 100.46457166},
#     'Mars': {'a': 2.279e8 / M_TO_AU, 'e': 0.0934, 'true_anomaly': -4.55343205},
#     'Jupiter': {'a': 7.785e8 / M_TO_AU, 'e': 0.0489, 'true_anomaly': 82.72354},
#     'Saturn': {'a': 1.434e9 / M_TO_AU, 'e': 0.0565, 'true_anomaly': 1.9},
#     'Uranus': {'a': 2.870972e9 / M_TO_AU, 'e': 0.04717, 'true_anomaly': 2.9},
#     'Neptune': {'a': 4.495e9 / M_TO_AU, 'e': 0.008678, 'true_anomaly': 0.9},
#     'Comet': {'a': 2.653e9 / M_TO_AU, 'e': 0.96658, 'true_anomaly': 45},
#
# }
# a_mercury = planetary_parameters['Mercury']['a']
# print(a_mercury)  # Output: 0.387 (in AU, if M_TO_AU = 1.496e11)
#

#Mercury parameters
a_merc = 0.3870984405809461
e_merc = 0.205630
b_merc = a_merc * np.sqrt(1 - e_merc ** 2)


#Venus Parameters
a_venus = 0.72333435702438364512
e_venus = 0.006772
b_venus = a_venus * np.sqrt(1 - e_venus ** 2)

#Earth parameters
a_earth = 0.9999096258460315
e_earth = 0.0167086
b_earth = a_earth * np.sqrt(1 - e_earth ** 2)

#Mars parameters
a_mars = 1.52366701961354
e_mars = 0.0934
b_mars = a_mars * np.sqrt(1 - (e_mars ** 2))

#Juptiter parameters
a_jupiter = 5.202615624829211
e_jupter =  0.0489
b_jupiter = a_jupiter * np.sqrt(1 - e_jupter ** 2)

#Saturn parameter
a_saturn = 9.55530091913267
e_saturn = 	0.0565
b_saturn = a_saturn * np.sqrt(1 - e_saturn ** 2)

#Uranus parameters
a_uranus = 19.29976484357809
e_uranus = 0.04717
b_uranus = a_uranus * np.sqrt(1 - e_uranus ** 2)

# Neptune parameters
a_neptune = 30.18345346368623
e_neptune = 0.008678
b_neptune = a_neptune * np.sqrt(1 - e_neptune ** 2)


# #Generate points for plot
vu = np.linspace(0, 2 * np.pi, 1000)


# #Mercury points and angle
x_merc = a_merc * np.cos(vu)
y_merc = b_merc * np.sin(vu)
mercury_xpoint = center[0] + a_merc * np.cos(3.470109933278747E-01)
mercury_ypoint = center[1] + b_merc * np.sin(3.470109933278747E-01)
mercury_x_jpl = 3.470109933278747E-01
mercury_y_jpl = 2.962928066778309E-02
theta_mercury= np.arctan2(mercury_y_jpl, mercury_x_jpl)
mercury_xpoint = a_merc * np.cos(theta_mercury)
mercury_ypoint = b_merc * np.sin(theta_mercury)


#Venus points and angle
x_venus = a_venus * np.cos(vu)
y_venus = b_venus * np.sin(vu)
venus_X_JPL = -4.792367698108020E-01
venus_Y_JPL = 5.341196737022612E-01
theta_venus = np.arctan2(venus_Y_JPL, venus_X_JPL)
venus_xpoint = a_venus * np.cos(theta_venus)
venus_ypoint = b_venus * np.sin(theta_venus)


#Earth points and angle
x_earth = a_earth * np.cos(vu)
y_earth = b_earth * np.sin(vu)
e_x_jpl = -8.668197727671992E-01
e_y_jpl = 4.756459233888252E-01
theta_earth = np.arctan2(e_y_jpl, e_x_jpl)
earth_xpoint = a_earth * np.cos(theta_earth)
earth_ypoint = b_earth * np.sin(theta_earth)

#Mars points and angle
x_mars = a_mars * np.cos(vu)
y_mars = b_mars * np.sin(vu)
m_x_jpl = -1.095266014558086E+00
m_y_jpl = 1.233808789811794E+00
theta_mars = np.arctan2(m_y_jpl, m_x_jpl)
mars_xpoint = a_mars * np.cos(theta_mars)
mars_ypoint = b_mars * np.sin(theta_mars)


#Jupiter points and angle
x_jupiter = a_jupiter * np.cos(vu)
y_jupiter = b_jupiter * np.sin(vu)
j_x_jpl = 6.796183204055646E-01
j_y_jpl = 5.053619648997143E+00
theta_jupiter = np.arctan2(j_y_jpl, j_x_jpl)
jupiter_xpoint =  a_jupiter * np.cos(theta_jupiter)
jupiter_ypoint =  b_jupiter * np.sin(theta_jupiter)

#Saturn points and angle
x_saturn = a_saturn * np.cos(vu)
y_saturn = b_saturn * np.sin(vu)
s_x_jpl = 9.492589419340332E+00
s_y_jpl = -1.490147033377904E+00
theta_saturn = np.arctan2(s_y_jpl, s_x_jpl)
saturn_xpoint = + a_saturn * np.cos(theta_saturn)
saturn_ypoint = b_saturn * np.sin(theta_saturn)

#Uranus points and angle
x_uranus = a_uranus * np.cos(vu)
y_uranus = b_uranus * np.sin(vu)
u_x_jpl = 1.093939104547853E+01
u_y_jpl = 1.619634452518559E+01
theta_uranus = np.arctan2(u_y_jpl, u_x_jpl)
uranus_xpoint = a_uranus * np.cos(theta_uranus)
uranus_ypoint = b_uranus * np.sin(theta_uranus)

#Neptune points and angle
x_neptune = a_neptune * np.cos(vu)
y_neptune = b_neptune * np.sin(vu)
n_x_jpl = 2.988147200499045E+01
n_y_jpl = -4.761611519619720E-01
theta_neptune = np.arctan2(n_y_jpl, n_x_jpl)
neptune_xpoint = a_neptune * np.cos(theta_neptune)
neptune_ypoint = b_neptune * np.sin(theta_neptune)


#plot
plt.figure(figsize=(10, 8))
#Setting sun to center
plt.scatter(0, 0, color='darkorange', s=100, label='Sun')

#Mercury orbit and position
plt.plot(x_merc, y_merc, label="Mercury Orbit", color='deeppink')
plt.scatter(mercury_xpoint, mercury_ypoint, color ='deeppink', s = 50)

#Venus orbit and position
plt.plot(x_venus, y_venus, label='Venus Orbit', color = 'mediumpurple')
plt.scatter(venus_xpoint, venus_ypoint, color ='mediumpurple', s = 50)

#Earth orbit and position
plt.plot(x_earth, y_earth, label='Earth Orbit', color = 'green')
plt.scatter(earth_xpoint, earth_ypoint, color ='green', s = 50)

#Mars orbit and position
plt.plot(x_mars, y_mars, label='Mars Orbit', color = 'red')
plt.scatter(mars_xpoint, mars_ypoint, color ='red', s = 50)

#Jupiter orbit and position
plt.plot(x_jupiter, y_jupiter, label='Jupiter Orbit', color = 'orange')
plt.scatter(jupiter_xpoint, jupiter_ypoint, color ='orange', s = 50)

#Saturn orbit and position
plt.plot(x_saturn, y_saturn, label = 'Saturn Orbit', color = 'yellow')
plt.scatter(saturn_xpoint, saturn_ypoint, color ='yellow', s = 50)

#Uranus postion and orbit
plt.plot(x_uranus, y_uranus, label = 'Uranus Orbit', color = 'palegreen')
plt.scatter(uranus_xpoint, uranus_ypoint, color ='palegreen', s = 50)

#Neptune position and orbit
plt.plot(x_neptune, y_neptune, label = 'Neptune Orbit', color = 'aqua')
plt.scatter(neptune_xpoint, neptune_ypoint, color ='aqua', s = 50)

# Labels and formatting
plt.xlabel("Distance (m)")
plt.ylabel("Distance (m)")
plt.title("Solar System")
plt.axis("equal")
plt.legend()
plt.grid()
# Set equal scaling for both axes
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')  # Apply a dark theme
from astroquery.jplhorizons import Horizons
from datetime import datetime, timedelta

# Get date for accrurate plots of planets
date_today = datetime.today().strftime('%Y-%m-%d')
date_tomorrow = (datetime.now()+ timedelta(days=1)).strftime("%Y-%m-%d")

# Data including semi-major axis and eccentricity of orbit
planetary_parameters = {
    'Mercury': {'a': 0.3870984405809461, 'e': 0.205630},
    'Venus': {'a': 0.72333435702438364512 , 'e': 0.006772,},
    'Earth': {'a': 0.9999096258460315 , 'e': 0.0167086},
    'Mars': {'a': 1.52366701961354 , 'e': 0.0934},
    'Jupiter': {'a': 5.202615624829211, 'e': 0.0489},
    'Saturn': {'a': 9.55530091913267, 'e': 0.0565},
    'Uranus': {'a': 19.29976484357809, 'e': 0.04717},
    'Neptune': {'a': 30.18345346368623, 'e': 0.008678}
}
# JPL ids for planets
body_ids = ['199', '299', '399', '499', '599', '699', '799', '899']

# Colours for plots
colours = ('deeppink', 'mediumpurple', 'green', 'red', 'orange', 'yellow', 'palegreen', 'aqua')

# Creates list to store values for coordinates

x_orbit = []
y_orbit = []
x_parameters, y_parameters = [], []
# Accesses JPL horizons database to get x, y coordinates of planets
for body_id in body_ids:
    obj = Horizons(id = body_id, location='500@10',epochs={'start': date_today, 'stop': date_tomorrow, 'step':'1d'})
    vec = obj.vectors()
    df = vec.to_pandas()
    df.drop(['datetime_jd','datetime_str','z' ,'vx', 'vy', 'vz', 'lighttime', 'range', 'range_rate'], axis = 1, inplace = True)
    x_parameters.append(float(df.loc[0, 'x']))
    y_parameters.append(float(df.loc[0, 'y']))
  
# Sets points for plots
vu = np.linspace(0, 2 * np.pi, 1000)

# Sets the center of the plot to 0,0
center = (0, 0)

# Acesses values in planetary paramters and calculates semi minor axis for planets
b_planets = []
def generate_plots():
    for i in planetary_parameters:
        b_planets.append(float(planetary_parameters[i]['a'] * np.sqrt(1 - planetary_parameters[i]['e'] ** 2)))
    return b_planets

# plots orbits
def plot_orbits(generate_plots):
    for (i, (planet, params)) in enumerate(planetary_parameters.items()):
        a = params['a']
        b = b_planets[i]
        x_orbit = a * np.cos(vu)
        y_orbit = b * np.sin(vu)
        theta = np.arctan2(y_parameters[i], x_parameters[i])
        x_points = a * np.cos(theta)
        y_points = b * np.sin(theta)
        plt.plot(x_orbit, y_orbit, color = colours[i], linestyle ='-')
        plt.scatter(x_points, y_points, color = colours[i], label = planet)

plot_orbits(generate_plots())

# Setting sun to center
plt.scatter(0, 0, color='darkorange', s=100, label='Sun')
plt.xlabel("Distance (Au)")
plt.ylabel("Distance (Au)")
plt.title("Solar System")
plt.axis("equal")
# Inside the plot_orbits function
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)  # Adjust position and font size
plt.grid()
# Set equal scaling for both axes
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

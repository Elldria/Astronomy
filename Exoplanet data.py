import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'C:\Users\ellio\OneDrive\Desktop\Python_CSV\Nasa exoplanet archive.csv')
pd.options.display.max_columns = 20
df.dropna(inplace = True)
print(df.columns)

#discoveryyear
# disc_year2 = df.loc[:, "disc_year"]
# plt.hist(disc_year2, bins=30)
# plt.title('Number of Exoplanet discoveries by year')
# plt.show()

stellar_mass = df.loc[:, 'st_mass']
planet_number = df.loc[:, 'sy_pnum']
star_number = df.loc[:, 'sy_snum']

# plt.scatter(stellar_mass, planet_number, marker = 'x', s = 5, color = 'red')
plt.hist2d(stellar_mass, planet_number)
# plt.xscale('log')
plt.show()


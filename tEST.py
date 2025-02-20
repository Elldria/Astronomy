
from astroquery.jplhorizons import Horizons
import pandas as pd
import matplotlib.pyplot as plt

obj = Horizons(id='199', location='500@0',epochs={'start':'2025-02-20', 'stop':'2025-02-21',
                       'step':'1d'})
vec = obj.vectors()
df = vec.to_pandas()
pd.set_option('display.max_columns', None)
print(df)


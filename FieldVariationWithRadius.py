import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.interpolate import CloughTocher2DInterpolator

# importing directly from excel into a pandas dataframe
datf = pd.read_excel("E:\\CodeMagfieldMap\\Data1excel.xlsx")
date = pd.read_excel("E:\\CodeMagfieldMap\\errorfile.xlsx")

x_data = datf['x'].to_numpy()
y_data = datf['y'].to_numpy()
field_data = datf['B'].to_numpy()

# importing error file
x_e = date['B'].to_numpy()
y_e = date['er'].to_numpy()

pe = interp1d(x_e, y_e, kind='cubic')
newer = pe(x_e)
#print(newer)
#print(len(newer))

# Conversion into cylindrical coordinates
rr = np.sqrt(x_data**2 + y_data**2)
tt_R = np.arctan2(y_data, x_data)

# 3d Interpolation
interp = CloughTocher2DInterpolator(list(zip(x_data, y_data)), field_data)
#z = interp(x,y)
tt_D = np.rad2deg(tt_R)
#print(tt_D)

# define theta range explicitly
ttD_range = np.linspace(start=0, stop=360, num=1000)

# field function calculates field at a point using interpolation function interp
def field(rr, ttD):
    field_at_point = (interp(rr * np.cos(ttD * np.pi / 180), rr * np.sin(ttD * np.pi / 180)) +
                      1 * pe(interp(rr * np.cos(ttD * np.pi / 180), rr * np.sin(ttD * np.pi / 180))) * 0.001)
    return field_at_point

plt.plot(ttD_range, field(50, ttD_range), 'c', label='r = 50')
plt.plot(ttD_range, field(60, ttD_range), 'b', label='r = 60')
plt.plot(ttD_range, field(70, ttD_range), 'r', label='r = 70')
plt.plot(ttD_range, field(80, ttD_range), 'g', label='r = 80')
plt.plot(ttD_range, field(90, ttD_range), 'y', label='r = 90')

plt.xlabel('Theta (degrees)')
plt.ylabel('Field Value (Kilo Gauss)')
plt.legend()
plt.title('Magnetic Field vs Theta (at different radii)')
plt.grid()
plt.show()

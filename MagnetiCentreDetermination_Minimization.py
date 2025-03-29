import numpy as np
from scipy.optimize import minimize

# RMSE function
def rmse(params, r_i, tt_i):
    r0, tt0 = params
    differences = r0 * np.cos(np.deg2rad(tt0) - np.deg2rad(tt_i)) - r_i
    return np.sqrt(np.mean(differences**2))

# Given values
ri_values = [1.8399, 2.1093, 1.336, 0.2851, -0.859, -1.9297, -1.8711]
tti_values = [0, 30, 60, 90, 120, 150, 180]

# Initial guess for parameters
init_guess = [2, 10]

# Minimize the RMSE function
res = minimize(rmse, init_guess, args=(ri_values, tti_values), method='Nelder-Mead')

# Print results
print("Minimum RMSE:", res.fun)
print("Optimal r0:", res.x[0])
print("Optimal tt0:", res.x[1])

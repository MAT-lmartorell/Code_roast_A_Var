# Standard libraries

# 3rd party libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Internal modules
from lluis.model import calculate_impulse_response
from lluis.shock import create_time_0_shock_vector
from lluis.visualize import plot_impulse_graphs

from marc.model import impulse_response
from marc.visualize import plot_graphs


# Common input
h = 8
shock_x = np.array([1, 0])
shock_y = np.array([0, 1])

### MARC workflow ---
# Input Marc specific
A_marc = {
    1: pd.DataFrame(
        [[0.5, 0.2], [0, 0.2]], columns=["x.shift(1)", "y.shift(1)"], index=["x", "y"]
    ),
    2: pd.DataFrame(
        [[0.2, 0], [-0.1, 0.3]], columns=["x.shift(2)", "y.shift(2)"], index=["x", "y"]
    ),
}
# Calculate
irf_x = impulse_response(A_marc, shock_x, h)
irf_y = impulse_response(A_marc, shock_y, h)
# Plot
marc_fig = plot_graphs(irf_x, irf_y)

### Lluis workflow ---
# Input Lluis specific
A1 = np.array([[0.5, 0.2], [0, 0.2]])
A2 = np.array([[0.2, 0], [-0.1, 0.3]])
A_lluis = np.array([A1, A2])
shock_vector_x = create_time_0_shock_vector(shock_x, h)
shock_vector_y = create_time_0_shock_vector(shock_y, h)
# Calculate
impulse_x = calculate_impulse_response(
    As=A_lluis, p=len(A1), shocks=shock_vector_x, max_time=h
)
impulse_y = calculate_impulse_response(
    As=A_lluis, p=len(A1), shocks=shock_vector_y, max_time=h
)
# Plot
lluis_fig_1 = plot_impulse_graphs(impulse_x, h)
lluis_fig_2 = plot_impulse_graphs(impulse_y, h)

### PLOT ---
plt.show()

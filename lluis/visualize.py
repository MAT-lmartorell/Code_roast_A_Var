# Standard libraries

# 3rd party libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Internal modules


def plot_impulse_graphs(impulse: list[np.ndarray], max_time: int) -> Figure:
    fig, ax = plt.subplots(nrows=2, ncols=1)
    # Vector preparation
    curve_x = np.arange(max_time + 1)
    curve_1_y = [y[0] for y in impulse]
    curve_2_y = [y[1] for y in impulse]

    ax[0].plot(curve_x, curve_1_y)
    ax[1].plot(curve_x, curve_2_y)

    return fig

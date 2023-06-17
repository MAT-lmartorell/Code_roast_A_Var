# Standard libraries

# 3rd party libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Internal modules


def plot_graphs(irf_x: pd.DataFrame, irf_y: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax[0, 0].plot(irf_x["x"])
    ax[0, 1].plot(irf_x["y"])
    ax[1, 0].plot(irf_y["x"])
    ax[1, 1].plot(irf_y["y"])

    return fig

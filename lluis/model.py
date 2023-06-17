# Standard libraries

# 3rd party libraries
import numpy as np

# Internal modules


def calculate_impulse_response(
    As: list[np.ndarray], p: int, shocks: list[np.ndarray], max_time: int
) -> list[np.ndarray]:
    # Initialize variables
    yts = list()
    # Solve until max_time
    for time in range(max_time + 1):
        shock = shocks[time]
        Y_vector = construct_Y_vector(yts, p)
        yt = next_t_impuls(As, Y_vector, p, shock)
        yts.append(yt)
    return yts


def construct_Y_vector(yts: list[np.ndarray], p: int) -> list[np.ndarray]:
    # Temp vector reversed
    reverse_yts = yts.copy()
    reverse_yts.reverse()
    # Initialize varibale
    Y_vector = list()
    # Create vector or add zero vector if missing yt-p in yts
    for i in range(p):
        try:
            previous_yt = reverse_yts[-1 - i]
        except IndexError:
            previous_yt = np.zeros(p)
        Y_vector.append(previous_yt)
    return Y_vector


def next_t_impuls(
    As: list[np.ndarray], Y_vector: list[np.ndarray], k: int, shock: np.ndarray
) -> np.ndarray:
    """TODO  use As or Y_Vector to define k inside function and remove from inputs!!!"""

    # Initialize next t impuls vector
    yt = np.zeros(k)
    # Multiply A matrices with yt-p vectors
    for A, y in zip(As, Y_vector):
        yt += np.dot(A, y)
    # Add shock
    yt += shock
    return yt

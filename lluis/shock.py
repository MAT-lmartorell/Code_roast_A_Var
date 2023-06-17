# Standard libraries

# 3rd party libraries
import numpy as np

# Internal modules


def create_time_0_shock_vector(
    initial_shock: np.ndarray, max_time: int
) -> list[np.ndarray]:
    # Initialize shock vector
    shock_vector = list()
    # Fill vector
    shock_vector.append(initial_shock)
    for _ in range(max_time):
        shock_vector.append(np.zeros(len(initial_shock)))
    return shock_vector

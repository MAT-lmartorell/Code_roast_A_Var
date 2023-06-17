# Standard libraries

# 3rd party libraries
import pandas as pd
import numpy as np

# Internal modules


def impulse_response(A: dict[pd.DataFrame], shock, h: int) -> pd.DataFrame:
    p = len(A)
    irs = pd.DataFrame(
        np.zeros((h + 1 + p, A[1].shape[0])), columns=A[1].index, index=range(-p, h + 1)
    )
    irs.index.name = "h"
    for ih in range(h + 1):
        if ih == 0:
            irs.loc[ih] = (
                np.sum([A[i] @ irs.loc[ih - i].values for i in range(1, p + 1)], axis=0)
                + shock
            )
        else:
            irs.loc[ih] = np.sum(
                [A[i] @ irs.loc[ih - i].values for i in range(1, p + 1)], axis=0
            )
    irs = irs.loc[0:]
    return irs

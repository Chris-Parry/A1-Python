import numpy as np
import numpy.typing as npt
import pandas as pd


def load_data(filepath):
    data: pd.DataFrame = pd.read_csv(filepath, delimiter=",", header=[0, 1])
    column_names = data.columns
    x_data: npt.NDArray = np.array(data[column_names[0]].values)
    y1_data: npt.NDArray = np.array(data[column_names[1]].values)
    y2_data: npt.NDArray = np.array(data[column_names[2]].values)
    return x_data, y1_data, y2_data

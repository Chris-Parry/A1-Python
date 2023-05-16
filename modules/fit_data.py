from typing import Any

import numpy as np
import numpy.typing as npt
from scipy.optimize import curve_fit


def sine_function(x, amplitude, frequency, phase_shift, vertical_shift) -> npt.NDArray:
    angular_frequency = frequency * 2 * np.pi
    y: npt.NDArray = (
        amplitude * np.sin(angular_frequency * x + phase_shift) + vertical_shift
    )
    return y


def fit_data(x_data, y1_data, y2_data, p01, p02) -> tuple[Any, Any, float, float]:
    params1, _ = curve_fit(sine_function, x_data, y1_data, p0=p01)
    params2, _ = curve_fit(sine_function, x_data, y2_data, p0=p02)
    phase_shift: float = np.abs(params1[2] - params2[2])
    phase_shift_degrees: float = np.degrees(phase_shift)
    return params1, params2, phase_shift, phase_shift_degrees

import numpy as np
import numpy.typing as npt
from scipy.optimize import curve_fit


def sine_function(x, amplitude, frequency, phase_shift, vertical_shift) -> npt.NDArray:
    angular_frequency = frequency * 2 * np.pi
    y: npt.NDArray = (
        amplitude * np.sin(angular_frequency * x + phase_shift) + vertical_shift
    )
    return y


def fit_data(x_data, y1_data, y2_data, p01, p02):
    params1, _ = curve_fit(sine_function, x_data, y1_data, p0=p01)
    params2, _ = curve_fit(sine_function, x_data, y2_data, p0=p02)
    phase_shift: float = np.abs(params1[2] - params2[2])
    phase_shift_degrees: float = np.degrees(phase_shift)
    print(f"Phase shift (radians): {phase_shift:.3f}")
    print(f"Phase shift (degrees): {phase_shift_degrees:.1f}")
    return params1, params2, phase_shift, phase_shift_degrees


# Load your data (two waves) from file
# filepath: str = "Data Files/scope_a1_0.csv"
# x_data, y_wave1, y_wave2 = load_data(filepath)
# print(f"x_data: {x_data}\n")
# print(f"y_wave1: {y_wave1}\n")
# print(f"y_wave2: {y_wave2}\n")


# Use curve-fitting algorithm to fit your data to the sine function

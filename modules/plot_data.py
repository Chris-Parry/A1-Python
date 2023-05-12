import os

from matplotlib import pyplot as plt

from modules.fit_data import sine_function


def plot_wave(
    x_data,
    y_data1,
    y_data2,
    fitted_y1,
    fitted_y2,
    filepath: str,
    phase_shift_degrees: float,
):
    filename = os.path.basename(filepath)
    plt.figure()
    plt.plot(x_data, y_data1, label="Wave 1")
    plt.plot(x_data, y_data2, label="Wave 2")
    plt.plot(x_data, sine_function(x_data, *fitted_y1), "--", label="Fitted Wave 1")
    plt.plot(x_data, sine_function(x_data, *fitted_y2), "--", label="Fitted Wave 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(
        f"Phase Shift: {phase_shift_degrees:.1f} degrees, with filepath: {filename}"
    )
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def main() -> None:
    def sine_function(x, amplitude, frequency, phase_shift, vertical_shift):
        return amplitude * np.sin(frequency * x + phase_shift) + vertical_shift

    # Function to load data from a file
    def load_data(filepath):
        data = pd.read_csv(filepath, delimiter=",", header=[0, 1])
        column_names = data.columns
        x_data = data[column_names[0]].values
        y1_data = data[column_names[1]].values
        y2_data = data[column_names[2]].values
        return x_data, y1_data, y2_data

    # Load your data (two waves) from file
    filepath = "Data Files/scope_a1_0.csv"
    x_data, y_wave1, y_wave2 = load_data(filepath)
    print(f"x_data: {x_data}\n")
    print(f"y_wave1: {y_wave1}\n")
    print(f"y_wave2: {y_wave2}\n")
    initial_guesses_wave1 = [
        0.3,  # Amplitude
        13.56e6,  # Frequency
        0,  # Phase shift
        0,  # Vertical shift
    ]
    initial_guesses_wave2 = [
        0.5,  # Amplitude
        13.56e6,  # Frequency
        0,  # Phase shift
        0,  # Vertical shift
    ]

    # Use curve-fitting algorithm to fit your data to the sine function
    params1, _ = curve_fit(sine_function, x_data, y_wave1, p0=initial_guesses_wave1)
    params2, _ = curve_fit(sine_function, x_data, y_wave2, p0=initial_guesses_wave2)

    # Calculate the phase shift between the two fitted sine waves
    phase_shift = np.abs(params1[2] - params2[2])

    # Convert phase shift to degrees
    phase_shift_degrees = np.degrees(phase_shift)

    # Print the phase shift in radians and degrees
    print(f"Phase shift (radians): {phase_shift:.3f}")
    print(f"Phase shift (degrees): {phase_shift_degrees:.1f}")

    # Write the phase shift information to a file
    output_file = "phase_shifts.txt"
    with open(output_file, "a") as f:
        f.write(f"File: {filepath}\n")
        f.write(f"Phase shift (radians): {phase_shift:.3f}\n")
        f.write(f"Phase shift (degrees): {phase_shift_degrees:.1f}\n")
        f.write("\n")

    # Plot the original waves and the fitted sine waves
    plt.figure()
    plt.plot(x_data, y_wave1, label="Wave 1")
    plt.plot(x_data, y_wave2, label="Wave 2")
    plt.plot(x_data, sine_function(x_data, *params1), "--", label="Fitted Wave 1")
    plt.plot(x_data, sine_function(x_data, *params2), "--", label="Fitted Wave 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

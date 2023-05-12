import matplotlib.pyplot as plt

from modules.fit_data import fit_data, sine_function
from modules.load_data import load_data
from modules.save_data import save_data


def main() -> None:
    filepath = "data/scope_a1_1.csv"
    x_data, y_wave1, y_wave2 = load_data(filepath)
    initial_guesses_wave1: list[float] = [
        0.3,  # Amplitude
        13.56e6,  # Frequency
        0,  # Phase shift
        0,  # Vertical shift
    ]
    initial_guesses_wave2: list[float] = [
        0.5,  # Amplitude
        13.56e6,  # Frequency
        0,  # Phase shift
        0,  # Vertical shift
    ]
    params_wave1, params_wave2, phase_shift, phase_shift_degrees = fit_data(
        x_data, y_wave1, y_wave2, initial_guesses_wave1, initial_guesses_wave2
    )
    save_data(filepath, phase_shift, phase_shift_degrees)
    plt.figure()
    plt.plot(x_data, y_wave1, label="Wave 1")
    plt.plot(x_data, y_wave2, label="Wave 2")
    plt.plot(x_data, sine_function(x_data, *params_wave1), "--", label="Fitted Wave 1")
    plt.plot(x_data, sine_function(x_data, *params_wave2), "--", label="Fitted Wave 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

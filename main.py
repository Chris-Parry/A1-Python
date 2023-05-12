from modules.fit_data import fit_data
from modules.load_data import load_data
from modules.plot_data import plot_wave
from modules.save_data import save_data


def main() -> None:
    filepath = "data/scope_a1_0.csv"
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
    plot_wave(
        x_data,
        y_wave1,
        y_wave2,
        params_wave1,
        params_wave2,
        filepath,
        phase_shift_degrees,
    )


if __name__ == "__main__":
    main()

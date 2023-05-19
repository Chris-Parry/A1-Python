import glob

from modules.fit_data import fit_data
from modules.load_data import load_data

# from modules.plot_data import plot_wave
from modules.save_data import save_data


def main() -> None:
    filepath = glob.glob("data/Oscilloscope Data/scope_a1_pw2_*[0-9].csv")
    filepath.sort()
    differences = []
    phase_shifts = []
    for file in filepath:
        x_data, y_wave1, y_wave2 = load_data(file)
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
        difference_in_degrees = 90 - phase_shift_degrees
        print(f"Phase shift (radians): {phase_shift:.3f}")
        print(f"Phase shift (degrees): {phase_shift_degrees:.1f}")
        print(f"Difference: {difference_in_degrees:.2f}")
        differences.append(difference_in_degrees)
        phase_shifts.append(phase_shift_degrees)
        # plot_wave(
        #     x_data,
        #     y_wave1,
        #     y_wave2,
        #     params_wave1,
        #     params_wave2,
        #     file,
        #     phase_shift_degrees,
        # )
        save_data(file, phase_shift, phase_shift_degrees, difference_in_degrees)
    avg_difference = sum(differences) / len(differences)
    print(f"Average phase shift: {sum(phase_shifts) / len(phase_shifts):.3f}")
    print(f"Average difference: {avg_difference:.2f}")


if __name__ == "__main__":
    main()

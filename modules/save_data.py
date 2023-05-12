def save_data(
    filepath: str,
    phase_shift: float,
    phase_shift_degrees: float,
):
    output_file: str = "phase_shifts.txt"
    with open(output_file, "a") as f:
        f.write(f"File: {filepath}\n")
        f.write(f"Phase shift (radians): {phase_shift:.3f}\n")
        f.write(f"Phase shift (degrees): {phase_shift_degrees:.1f}\n")
        f.write("\n")

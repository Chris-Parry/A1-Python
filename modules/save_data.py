def save_data(
    filepath: str,
    phase_shift: float,
    phase_shift_degrees: float,
    difference_in_degrees: float,
) -> None:
    output_file: str = "phase_shifts.txt"
    new_content = (
        f"File: {filepath}\n"
        f"Phase shift (radians): {phase_shift:.3f}\n"
        f"Phase shift (degrees): {phase_shift_degrees:.1f}\n"
        f"Difference: {difference_in_degrees:.2f}\n"
        "\n"
    )
    with open(output_file, "r") as f:
        existing_content = f.read()
    if new_content not in existing_content:
        with open(output_file, "a") as f:
            f.write(new_content)

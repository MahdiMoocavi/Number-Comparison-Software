"""Two-choice numerical magnitude comparison experiment implemented in PsychoPy.

Participants judge which of two numbers is larger. Each randomly paired number
set is presented in both left-right configurations. Trial-level responses,
reaction times, and accuracy are saved to results.csv.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from psychopy import core, event, visual


def build_trial_pairs(seed=None):
    """Create 40 trials from the integers 1–40, with each pair reversed once."""
    rng = np.random.default_rng(seed)
    numbers = np.arange(1, 41)
    rng.shuffle(numbers)

    original_pairs = numbers.reshape(20, 2)
    reversed_pairs = original_pairs[:, ::-1]
    trial_pairs = np.vstack((original_pairs, reversed_pairs))
    rng.shuffle(trial_pairs)
    return trial_pairs


def run_experiment(output_path=None):
    """Run the task and save one row per trial."""
    output_path = Path(output_path) if output_path else Path(__file__).resolve().parent / "results.csv"
    trial_pairs = build_trial_pairs()
    records = []

    window = visual.Window(fullscr=False, color=(-1, -1, -1), units="pix")
    clock = core.Clock()

    try:
        instructions = visual.TextStim(
            window,
            text=(
                "Numerical comparison task\n\n"
                "Two numbers will appear on the screen. Choose the larger number.\n"
                "Press F if the left number is larger.\n"
                "Press J if the right number is larger.\n\n"
                "Please respond as quickly and accurately as possible.\n\n"
                "Press ENTER to begin."
            ),
            color=(1, 1, 1),
            height=24,
            wrapWidth=1000,
        )
        instructions.draw()
        window.flip()
        event.waitKeys(keyList=["return"], clearEvents=True)

        fixation = visual.TextStim(window, text="+", color=(1, 1, 1), height=36)
        fixation.draw()
        window.flip()
        core.wait(2.0)

        for trial_number, (left_number, right_number) in enumerate(trial_pairs, start=1):
            pair_text = visual.TextStim(
                window,
                text=f"{left_number}                         {right_number}",
                color=(1, 1, 1),
                height=42,
            )
            divider = visual.Line(
                window,
                lineColor=(1, 1, 1),
                lineWidth=2,
                start=(0, -35),
                end=(0, 35),
            )

            pair_text.draw()
            divider.draw()
            clock.reset()
            window.flip()

            response = event.waitKeys(
                keyList=["f", "j"],
                timeStamped=clock,
                clearEvents=True,
            )
            response_key, response_time = response[0]

            correct_key = "f" if left_number > right_number else "j"
            accuracy = int(response_key == correct_key)

            records.append(
                {
                    "trial": trial_number,
                    "left_number": int(left_number),
                    "right_number": int(right_number),
                    "response_key": response_key,
                    "correct_key": correct_key,
                    "response_time_sec": float(response_time),
                    "accuracy": accuracy,
                }
            )

            if response_time > 1.0:
                feedback = visual.TextStim(
                    window,
                    text="Please try to respond faster.",
                    color=(1, 1, 1),
                    height=24,
                )
                feedback.draw()
                window.flip()
                core.wait(1.0)

        ending = visual.TextStim(
            window,
            text="Thank you for your participation!",
            color=(1, 1, 1),
            height=26,
        )
        ending.draw()
        window.flip()
        core.wait(2.0)

    finally:
        window.close()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    results = pd.DataFrame.from_records(records)
    results.to_csv(output_path, index=False)
    return results


if __name__ == "__main__":
    run_experiment()

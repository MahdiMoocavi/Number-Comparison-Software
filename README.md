# Numerical Magnitude Comparison Task

A compact PsychoPy experiment implementing a two-choice numerical magnitude judgment task. Each participant completes 40 trials: 20 randomly formed number pairs, each presented in both left–right configurations.

## Task design

- Samples the integers 1–40 and forms 20 non-overlapping pairs.
- Presents each pair in its original and reversed left–right configuration.
- Randomizes trial order.
- Collects responses using **F** (left number larger) and **J** (right number larger).
- Records one structured row per trial, including stimulus values, response, correct response, reaction time, and accuracy.

## Requirements

Python, PsychoPy, NumPy, and pandas.

```bash
pip install psychopy numpy pandas
```

## Run

```bash
python numerical_magnitude_task.py
```

The task opens a PsychoPy window and waits for Enter before beginning. Trial-level results are saved to `results.csv` in the script directory.

## Scope

This is a focused experimental implementation rather than a packaged application. It demonstrates stimulus generation, counterbalanced left–right presentation, response collection, reaction-time measurement, accuracy scoring, and structured data export. The task does not currently include a formal practice phase, participant metadata dialog, or automated analysis/reporting.

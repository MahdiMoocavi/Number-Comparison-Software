# Numerical Magnitude Comparison Task

A small PsychoPy experiment for studying numerical magnitude judgments. On each trial, participants view two numbers and indicate which number is larger.

## Task design

- Generates pairs from the integers 1–40 and includes reversed left–right presentations.
- Presents the pair on screen with a central fixation line.
- Participants press **F** when the left number is larger and **J** when the right number is larger.
- Records the selected key and response time.
- Displays a reminder when the response time exceeds one second.

## Requirements

- Python
- PsychoPy
- NumPy
- pandas

Install the Python dependencies with:

```bash
pip install psychopy numpy pandas
```

## Run

From the repository directory:

```bash
python numerical_magnitude_task.py
```

The task opens a PsychoPy window and waits for the participant to press Enter before starting.

## Data output

The script attempts to export the collected information to `results.csv` in the working directory.

## Current scope and limitations

This is an early experimental implementation rather than a packaged application. The current script does not calculate trial-level accuracy, does not set or record a random seed, and combines the stimulus matrix and response records in a way that should be normalized before the CSV is treated as an analysis-ready trial table. These are appropriate targets for a future code-quality pass.

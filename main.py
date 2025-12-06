"""
main.py

Entry point for the DS-AP capstone project:
"Predicting Excess Returns in the Automobile Industry Using Machine Learning".

Running:
    python main.py

will:
    1) Run the single train–test split experiment
    2) Run the walk-forward expanding-window experiment
and save all results under outputs/ (figures + CSV artifacts).

Modules used:
    - auto_ml_pkg.run_experiment_single_split
    - auto_ml_pkg.run_experiment_walkforward
"""

import os
import sys

# ---------------------------------------------------------------------
# 0) Ensure project root is on sys.path
# ---------------------------------------------------------------------
# CURRENT_DIR = location of this file (project root: auto_ml/)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) 

if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# Now we can import from auto_ml_pkg.*
from auto_ml_pkg.run_experiment_single_split import main as run_single_split
from auto_ml_pkg.run_experiment_walkforward import main as run_walkforward


def main() -> None:
    """
    High-level orchestration of the two experiments:
    1) Single train–test split
    2) Walk-forward expanding-window evaluation
    """

    print("=" * 70)
    print(" DS-AP Capstone Project – Excess Returns in the Auto Industry")
    print(" Entry point: main.py")
    print("=" * 70)
    print()

    # -----------------------------------------------------------------
    # 1) Single Train–Test Split
    # -----------------------------------------------------------------
    print(">>> 1/2 Running SINGLE TRAIN–TEST SPLIT experiment...")
    try:
        run_single_split()
        print(">>> Single split experiment completed successfully.\n")
    except Exception as e:
        print("\n[ERROR] Single split experiment failed:")
        print(repr(e))
        # You can choose to return here if you prefer to stop everything
        # return

    # -----------------------------------------------------------------
    # 2) Walk-Forward Expanding-Window Experiment
    # -----------------------------------------------------------------
    print(">>> 2/2 Running WALK-FORWARD experiment (expanding window)...")
    try:
        run_walkforward()
        print(">>> Walk-forward experiment completed successfully.\n")
    except Exception as e:
        print("\n[ERROR] Walk-forward experiment failed:")
        print(repr(e))

    print("=" * 70)
    print(" All experiments finished. Check the 'outputs/' directory for:")
    print("   - figures/   (equity curves, scatter plots, benchmark charts)")
    print("   - artifacts/ (CSV predictions, realized returns, metrics)")
    print("=" * 70)


if __name__ == "__main__":
    main()
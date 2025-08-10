# biomech-data-toolkit

**A Python toolkit for loading, filtering, and analyzing biomechanical joint angle data**

---

## Overview

This project provides essential tools for pre-processing and analyzing biomechanical signals collected during human movement experiments. It includes functions to:

- Load joint angle time-series data from CSV files
- Apply Butterworth low-pass filtering to reduce noise
- Extract clinically relevant features such as range of motion (ROM)
- Visualize raw and processed signals with publication-quality plots

The toolkit is built with usability and reproducibility in mind, making it suitable for biomedical engineering students and researchers working on gait analysis, orthopedics, and rehabilitation studies.

---

## Features

- **Data Loading:** Robust CSV data import with pandas
- **Signal Processing:** Zero-phase Butterworth low-pass filtering using SciPy
- **Feature Extraction:** Simple biomechanical metrics (e.g., range of motion)
- **Visualization:** Matplotlib-based plotting of raw and filtered signals
- **Modular Structure:** Easily extensible Python package format

---

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/zoyahhh13/biomech-data-toolkit.git
   cd biomech-data-toolkit

# create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows PowerShell

# install dependencies
   python -m pip install -r requirements.txt

# load and filter data
   from src.data_loader import load_csv
   from src.signal_processing import lowpass_filter
   from src.features import range_of_motion
   import matplotlib.pyplot as plt
   
# Load sample data
df = load_csv('data/sample_data.csv')

# Filter knee joint angle
filtered_knee = lowpass_filter(df['ankle_angle_knee'], cutoff=6, fs=100)

# Plot raw vs filtered
plt.plot(df['time'], df['ankle_angle_knee'], label='Raw')
plt.plot(df['time'], filtered_knee, label='Filtered')
plt.xlabel('Time (s)')
plt.ylabel('Knee Angle (degrees)')
plt.legend()
plt.show()

# Calculate range of motion
rom_knee = range_of_motion(filtered_knee)
print(f"Knee Range of Motion: {rom_knee:.2f} degrees")

# project structure
biomech-data-toolkit/
├── data/               # Sample and experimental CSV data files
├── notebooks/          # Jupyter notebooks for demos and analysis
├── src/                # Python source code modules
│   ├── data_loader.py
│   ├── signal_processing.py
│   └── features.py
├── requirements.txt    # Project dependencies
├── README.md           # Project overview and usage instructions
└── LICENSE             # MIT License

# contributing 
Contributions are welcome! Please open an issue or submit a pull request to discuss improvements, bug fixes, or new features.

# license
this project is licensed under the MIT License — see the LICENSE file for details.

# contact 
Created by Zoya Fatima — aspiring biomedical engineer and pre-med student at UT Austin.

Feel free to reach out via GitHub or email at zoyafatima@utexas.edu.

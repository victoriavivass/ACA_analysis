# Data Science Programming – PEC4  
**Author:** María Victoria Vivas Gutiérrez  
**Submission Date:** June 2025  

## Project Overview  
This project was developed as the **final evaluation for the course *Programming for Data Science*** at the Universitat Oberta de Catalunya (UOC).  

It was carried out during my **gap year**, while preparing and applying for a Master's program, as a way to consolidate my skills in Python, modular programming, testing, and data analysis.  

The main objective is to build a **modular Python package** to analyze the water volume of the **La Baells Reservoir** using real open data from the *Agència Catalana de l’Aigua (ACA)*.  
The project is structured into five modules, each covering different analysis tasks and functionalities: data loading, cleaning, transformations, smoothing, and drought period detection.  

---

## Installation  

Clone the repository and install dependencies:  
```bash
git clone https://github.com/victoriavivass/ACA_analysis.git
cd ACA_analysis
pip install -r requirements.txt
```
Run the complete analysis:

```bash
python main.py
```
Run a specific module (e.g. up to module 3):

 ```bash
 python main.py -ex 3
```
## Project Structure

```
ACA_analysis/
│── img/                     # Generated plots and images
│── test/                    # Unit tests
│   ├── test_modulo1.py
│   ├── test_modulo2.py
│   ├── test_modulo3.py
│   ├── test_modulo4.py
│   ├── test_modulo5.py
│── modulo1.py               # Data loading and exploration
│── modulo2.py               # Data cleaning and filtering
│── modulo3.py               # Temporal transformations & visualization
│── modulo4.py               # Data smoothing & trends
│── modulo5.py               # Drought period detection
│── main.py                  # Entry point for the analysis
│── requirements.txt         # Project dependencies
│── README.md                # Project documentation
```
## Modules & Functionality

### 1. Data Loading & Exploration (Module 1)
- Fetch dataset from the ACA API and load into a Pandas DataFrame.
- Display the first five rows for an initial preview.
- Show the general structure of columns.
- Print a summary of the DataFrame using `df.info()`.

### 2. Data Cleaning & Filtering (Module 2)
- Rename columns using a dictionary for clarity.
- Normalize reservoir names using regular expressions.
- Filter data specifically for the La Baells Reservoir.

### 3. Temporal Transformations & Visualization (Module 3)
- Convert the dia column to `datetime` type.
- Sort dataset chronologically for easier interpretation.
- Identify the earliest and most recent dates in the dataset.
- Create `dia_decimal` column (decimal representation of dates).
- Plot reservoir water volume over time and save it under `img/`.

### 4.  Data Smoothing & Trend Analysis (Module 4)
- Apply `savgol_filter` (from scipy) to smooth fluctuations in reservoir volume.
- Compare original vs. smoothed signals in a plot.
- Save the generated plot in `img/` including the student’s name.
  
### 5. Drought Period Detection (Module 5)
- Implement calcula_periodos() function to detect drought periods.
- Define droughts as periods when storage percentage drops below 60%.
- Print detected periods as a list with start and end dates.



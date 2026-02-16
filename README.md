# TOPSIS Assignment – Multi Criteria Decision Making

##  Overview
This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method using Python.

TOPSIS is a **Multi-Criteria Decision Making (MCDM)** technique used to rank alternatives based on their distance from the ideal best and ideal worst solutions.

The project is divided into three parts:

1. Understanding and implementing TOPSIS mathematically  
2. Creating a Python package and command line tool  
3. Developing a web interface for TOPSIS evaluation  

---

## Part 1 – Mathematical Implementation

### Steps of TOPSIS Algorithm
1. Construct decision matrix  
2. Normalize the matrix  
3. Multiply by weights  
4. Determine ideal best and ideal worst  
5. Calculate distance from ideal solutions  
6. Compute TOPSIS score and rank alternatives  

---

### Dataset Used

| Fund | P1 | P2 | P3 | P4 | P5 |
|----|----|----|----|----|----|
| M1 | 0.70 | 0.75 | 5.3 | 51.8 | 14.2 |
| M2 | 0.82 | 0.78 | 6.2 | 48.5 | 11.6 |
| M3 | 0.77 | 0.71 | 5.9 | 60.7 | 16.8 |
| M4 | 0.91 | 0.86 | 4.2 | 45.0 | 10.9 |
| M5 | 0.73 | 0.65 | 4.6 | 57.4 | 15.4 |
| M6 | 0.85 | 0.81 | 6.6 | 39.2 | 10.1 |
| M7 | 0.93 | 0.89 | 3.7 | 46.8 | 12.5 |
| M8 | 0.80 | 0.74 | 6.1 | 49.9 | 13.6 |

---

### Output Result

| Fund | Topsis Score | Rank |
|----|----|----|
| M3 | 0.7039 | 1 |
| M8 | 0.5820 | 2 |
| M2 | 0.5242 | 3 |
| M1 | 0.5113 | 4 |
| M5 | 0.5045 | 5 |
| M6 | 0.4714 | 6 |
| M7 | 0.4121 | 7 |
| M4 | 0.3662 | 8 |

---

## Part 2 – Python Package

A Python package was created to run TOPSIS directly from terminal.

### Installation

pip install topsis_kanika_102313062-1.0.0-py3-none-any.whl
topsis <InputDataFile> <Weights> <Impacts> <OutputFile>


## Part 3 – Web Implementation

A Flask-based web application was developed where users can:

- Upload dataset (CSV)
- Enter weights & impacts
- Provide email ID
- Receive ranked result via email

---

## Validation Rules

- Dataset must contain numeric criteria
- Minimum 3 columns required
- Weights count must equal criteria count
- Impacts must be '+' or '-'
- Valid email format required

---

## Technologies Used

- Python
- NumPy
- Pandas
- Flask
- HTML
- SMTP Email Service

---

## Conclusion

The TOPSIS method successfully ranked alternatives based on multiple criteria.

The same results were verified using:

- Python script
- Python package
- Web interface

This confirms correctness and reliability of the implementation.

---

## Author

**Kanika Dhamija**  
Roll Number: 102313062  
Email: kkanika1_be23@thapar.edu




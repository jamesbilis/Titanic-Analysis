# Titanic Data Exploratory Analysis

This project performs exploratory data analysis on the Titanic dataset using Python and popular data science libraries. The goal is to uncover patterns in survival rates based on age, gender, class, and other features.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Key Features

- Cleaned missing data (e.g., age) and handled outliers using Z-score filtering
- Visualized survival rates by gender, age group, passenger class, and embarkation point
- Generated heatmaps and bar plots to show correlations between variables
- Provided narrative commentary alongside charts to explain findings

## Project Structure

```
titanic-analysis/
│
├── titanic_eda.ipynb           # Jupyter notebook with full analysis
├── titanic.csv                 # Dataset file
├── images/                     # Visuals exported from notebook
└── README.md                   # Project overview
```

## Sample Visualizations

![Survival Rate by Gender](images/survival_gender.png)
![Age Distribution](images/age_distribution.png)

## How to Run

1. Clone the repository  
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Launch the notebook:
   ```bash
   jupyter notebook titanic_eda.ipynb
   ```

## License

MIT License

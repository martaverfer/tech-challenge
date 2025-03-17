# Portfolio Analysis

## Project Overview

This project involves the evaluation of investment portfolios to optimize asset allocation and management. It takes a variety of financial metrics and visualizations to assess the performance and risk of different financial assets. The dataset provided contains the asset returns and portfolio weights over three years.

## Objectives 

- Perform a series of calculations and create visualizations to analyze a set of financial assets.
- Get the normalized assets prices over time
- Daily Percentage Returns Calculation
- Portfolio Analysis: Cumulative Returns, Annualized Return, Annualized Volatility.
- Portfolio Analysis visualizations

## Methodology

1. **Data Cleaning:**
- Handle missing values.
- Formatting.
- Normalize or standarize numerical values where necessary to ensure compatibility for analysis and modeling.
2. **Exploratory Data Analysis (EDA):**
- Analyze summary statistics to identify patterns, trends, anomalies.
- Use various visualization techniques to better inderstand the distribution and relationships between the variables.
3. **Statistical Analysis:**
- Conduct correlation analysis to identify significant relationships between assets.

## Installation

To run this project locally, follow these instructions:

1. **Clone this repository:**

```bash
git clone https://github.com/martaverfer/project-data-analysis.git \
cd src
```

2. **Virtual environment:**

Create the virtual environment: 
```bash
python3 -m venv venv
```

Activate the virtual environment:

- For Windows: 
```bash
venv\Scripts\activate
```

- For Linux/Mac: 
```bash
source venv/bin/activate
```

To switch back to normal terminal usage or activate another virtual environment to work with another project run:
```deactivate```

3. **Install dependencies:**

```bash
pip install --upgrade pip; \
pip install -r requirements.txt
```

4. **Open the Jupyter notebook to explore the analysis:**

```bash
cd src; \
Tech-Challenge.ipynb
```

This script will execute the analysis steps and produce the results.

## Analysis and Results

- There is a strong positive correlation between the Daily Percentage Return of Asset2 and Asset3.
- Asset4 and Asset 2 incresed their weight the most at the end of the period, compared with the rest of the assets.
- Overall Portfolio Growth: the portfolio has increased as the cumulative return at the end of the period is higher than at the beggining.
- The Historical Cumulative Returns of the Portfolio does not show sharp spikes. It shows a continious growth, with the drawdown exception during 2020-04 (probably COVID related).
- The Annualized Portfolio return is 8.09%, which indicates a good return.
- The Annualized Volatility is moderate (8.51%), which indicates that the portfolio has some fluctuations.
- Fixed Income and Alternative families show a similar behaviour, whereas Equity and Fixed Income show an opposite performance. 

## Conclusion

This project provides insights into portfolio analysis, focusing on how asset weights change over time, calculating returns, and visualizing data. By following this approach, portfolio managers can track and optimize asset allocations.

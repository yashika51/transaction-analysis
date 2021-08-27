# transaction-analysis
Analysis of transactions from dummy data

Hello, this repositpory contains initial analysis based on the transaction data. 

### How to run this locally?

The best way to run this is to:
- create a virtual environment
- install all requirements including `pandas`, `matoplotlib`, `requests`, `sqlite3`,`django`,`wordcloud`.
- clone this repo
- `cd` to transaction-analysis 
- run the desired scripts

### Overview of all the scripts:

1. `process_data.py`: This is the most crucial script with the functions to get and process data for analysis. Functions from this script are used by other scripts
2. `insert_data_db.py`: This simple script inserts the monthly  monthly expense data per category to the database. The data is extracted from the function `monthly_expenses_per_category()`. Supporting model is created under `expense_data/models`.
3. `plot_insights.py`: This script contains functions to plot data and deliver insights to the user. We can call functions for the data we need to see and moving forward these functions can be called accorfingly.


### Checks and formatters:

The scripts have been run against `black` completely and `pylint` partially. 





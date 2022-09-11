## Table of Contents
1. [General Info](#general-info)
2. [Installation](#installation)

### General Info
***
This repository contains:
  * A **Python Jupyter notebook** `Energy_Demand_Forecast.ipynb` file detailing full analysis process for the UK daily energy consumption data. The time series dataset `energy.dat` 
    contains 5 years history. The notebook contains:
    * Data features identification
    * Data treatment process and tests
    * Daily Demand forecasting for next 12-months period and plots
    
  * There is also a Python script file `odd_coin_combination.py` to help solve the **odd coin combination problem**, see below. 
      * The algorithm accepts any amount of notes or coins, and dispensing equal value of coins for change. The coins available in this machine are: **Two Pounds, One  Pound, 50 Pence, 20 Pence, 10 Pence, 5 Pence, 2 Pence and 1 Pence**. The quantity of each type of coin is unlimited. The order of coins does not matter.
      * Units tests can be found in `tests/tests_odd_coin_combination.py`
```
Input: a STRING represents money value in below format:
 £{Pound}-{Pence} 

For Example, £2-30

Output: The number of solutions, which has odd coin count.

For Example
£0-5 can be changed to below
[£0-1, £0-1, £0-1, £0-1, £0-1]
[£0-1, £0-1, £0-1, £0-2]
[£0-1, £0-2, £0-2]
{£0-5}

Therefore, the Output for £0-5 must be 3.
• Compute follow inputs: £0-50, £2-, £10-, (£100- for extra marks)

Current output:
#Total odd coin count that sum to £0-50 = 225

#Total odd coin count that sum to £2-0 =  36840

#Total odd coin count that sum to £10-0 = 160667940
```

## Installation
***
The files can be  intro about the installation. 
```
git clone https://github.com/svm9000/Tests.git

```
Code was run on `Python version 3.10.4` using Visual Studio Code IDE, see [Visual Studio Code](https://code.visualstudio.com/), with Jupyter notebook support installed. To reproduce environment it is recommended to create your own virtual environment, see [virtualenv](https://virtualenv.pypa.io/en/stable/). Then install the required packages using `pip install -r requirements.txt`. We can also run the programs within a docker container, see [docker](https://docs.docker.com/language/python/build-images/).


# INF601 - Advanced Programming in Python
# Iris Perry
# Mini Project 1

# PLEASE WATCH THE VIDEO FOR THIS BEFORE STARTING!
#
# Please submit a link to your GitHub project. Do not submit your project files here.
#
# This project will be using the packages NumPy and Matplotlib in order to create 5 graphs that output as PNG files.
#
#     (5/5 points) Initial comments with your name, class and project at the top of your .py file.
#     (5/5 points) Proper import of packages used.
#     (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#     (10/10 points) Store this information in a list that you will convert to an array in NumPy.
#     (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum, it just needs to show 10 data points.
#     (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#     (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#     (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
#     (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import copy

mystocks = ['MSFT', 'AAPL', 'GOOG', 'NVDA', 'WMT']
mystockdata = {}

for stock in mystocks:
    dat = yf.Ticker(stock)
    last10 = dat.history(period='10d')
    mystockdata[stock] = []

    # Create a list of Closing Prices
    for price in last10['Close']:
        mystockdata[stock].append(price)
    mystock = np.array(mystockdata[stock])

    # Create variable to determine HIGH and LOW in time period
    hl = copy.copy(mystockdata[stock])
    hl.sort()

    # Generate graphs
    plt.plot(mystock)
    plt.title(stock)
    plt.axis((0, 10, hl[0]-10, hl[-1]+10))
    plt.ylabel('Closing Price')
    plt.xlabel('Trading Days Ago')
    plt.savefig(f'charts/{stock}.png')
    plt.show()

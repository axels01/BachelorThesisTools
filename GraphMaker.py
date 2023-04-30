'''
Axel Östergren 2023-04-26

This script is written as part of a bachelor thesis project
by Axel Östergren and Arvid Albinsson at Högskolan Väst
in Trollhättan, Sweden.

The script is free to use and can be modified
by anyone. The script is provided as is and the authors
take no responsibility for any damage caused by the script.
'''
import os
import sys
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm


#Simple file reader
def readFile(fileName):
    with open(fileName, newline='') as file:
        data = []
        for row in file:
            try:
                 data.append(float(row))
            except:
                #if the row cant be converted to float skip
                print("Could not convert to float: " + row)
                pass  
    return data

def writeFile(data, fileName):
    fileName = fileName.split('.')[0] + "_results.txt"
    with open(fileName, 'w') as file:
        for row in data:
            file.write(str(row) + '\n')

#creates a normal distribution graph from the data in the file
#has default values for title, x and y labels and bins which can
#be changed by the user if the initial graph looks good
def normalDistribution(data, title="Normal distribution", xlabel="X", ylabel="Y", bins=10, save=False, filename="NormalDistribution.png"):
    plt.clf()
    plt.hist(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(fileName.split('.')[0] + "_normalDistr.png")


def normalProbablity(data, title="QQ Plot", xlabel="X", ylabel="Y", line='45', save=False, filename="QQPlot.png"):
    plt.clf()
    data = np.log(np.array(data))
    fig = sm.qqplot(data, line=line)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(fileName.split('.')[0] + "_QQPlot.png")



#driver code
if __name__ == '__main__':
    opitons = ["1. All tests (exported)", "2. Shapiro-Wilk and Anderson-Darling tests", "3. Skewness and kurtosis", "4. Normal probability plot (Q-Q)", "5. Normal distribution graph"]
    #prints cwd as a reminder to the user where the script is looking for files
    print("cwd: " + os.getcwd())
    
    fileName = input("Data file name (no spaces): ")
    #if the file does not exist, exit the script
    if not os.path.exists(fileName):
        sys.exit("The file does not exist")
    data = readFile(fileName)

    for option in opitons:
        print(option)
    option = input("Select an option: ")

    if option == '1':
        results = []
        shapiro = stats.shapiro(data)
        anderson = stats.anderson(data)
        results.append("Shapiro-Wilk test: " + "W: " + str(shapiro[0]) + " p-value: " + str(shapiro[1]))
        results.append("Anderson-Darling test: " + "A^2: " + str(anderson[0]) + " p-value: " + str(anderson[1]))
        results.append("Skewness: " + str(stats.skew(data)))
        results.append("Kurtosis: " + str(stats.kurtosis(data)))
        writeFile(results, fileName)

        normalProbablity(data, "QQ Plot", "X", "Y", 's', True, fileName)
        normalDistribution(data, "Normal distribution", "X", "Y", 5, True, fileName)



    elif option == '2':
        shapiro = stats.shapiro(data)
        anderson = stats.anderson(data)

        print("Shapiro-Wilk test: " + "W: " + str(shapiro[0]) + " p-value: " + str(shapiro[1]))
        print("Anderson-Darling test: " + "A^2: " + str(anderson[0]) + " p-value: " + str(anderson[1]))

    elif option == '3':
        print("Skewness: " + str(stats.skew(data)))
        print("Kurtosis: " + str(stats.kurtosis(data)))

    elif option == '4':
        print("Normal probability plot (Q-Q):")
        line = input("Line (45, s, q): ")
        if line not in ['45', 's', 'q']:
            sys.exit("unsupported line argument")

        normalProbablity(data, line=line)

    elif option == '5':
        print("Normal distribution graph:")
        bin = input("Bin: ")
        #if the user does not enter an integer, exit with error
        try:
            bin = int(bin)
        except:
            sys.exit("Bin was not an integer, using default value: 10")  

        #creates a normal distribution graph from the data in the file
        normalDistribution(data, bins=bin)
        title = input("Title of graph: ")
        xlabel = input("X label: ")
        ylabel = input("Y label: ")
        normalDistribution(data, title, xlabel, ylabel, bins=bin)
    else:
        sys.exit("Unsupported option")
'''
Axel Östergren 2023-05-01

This script is written as part of a bachelor 
thesis project by Axel Östergren and Arvid Albinsson 
at Högskolan Väst in Trollhättan, Sweden.

The script is free to use and can be modified
by anyone. The script is provided as is and the authors
take no responsibility for any damage caused by the script.
'''

import sys
import pandas as pd
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#Turns data (dframe) into usable format for seaborn 
def melt(dFrame):
    dFrame = pd.melt(dFrame.reset_index(), id_vars=['index'], value_vars=['V', 'S','T'])
    #Changes column names 
    dFrame.columns = ['index', 'Navigeringsmetod', 'Värde']
    return dFrame

#Plots data, first row draws the boxplot, second row inserts the dots (data points)
def boxPlot(dFrame, title = ""):
    sns.boxplot(x='Navigeringsmetod', y='Värde', data=dFrame)
    sns.swarmplot(x="Navigeringsmetod", y="Värde", data=dFrame)
    plt.title("Boxplot " + title)
    plt.show()
    
#Plots qq-plot
def qq(dFrame, title = ""):
    for index in dFrame:
        sm.qqplot(dFrame[index], line='s')
        #adds title
        plt.title("Q-Q " + title + " " + index)
        plt.show()

def histogram(dFrame, title = ""):
    for index in dFrame:
        sns.histplot(
            dFrame[index], kde=True,
            stat="density", kde_kws=dict(cut=3),
            alpha=.4, edgecolor=(1, 1, 1, .4))
        plt.title("Histogram " + title + " " + index)
        plt.show()

#Shapiro-Wilk test
def shapiro(dFrame):
    for index in dFrame:
        shp = stats.shapiro(dFrame[index]) 
        print("Shapiro-Wilk test " + index + ": p-value: " + 
              str(shp.pvalue) + ", W-value: " + str(shp.statistic))

#one-way anova
def anova(dFrame, rt = False):
    model = ols('Värde ~ C(Navigeringsmetod)', melt(dFrame)).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    #functionality for return when called from resid()
    if rt:
        return model.resid
    else:
        print(anova_table)

#residual qq plot
def resid(dFrame, title = ""):
    sm.qqplot(anova(dFrame, True), line='s')
    plt.title("Residual Q-Q " + title)
    plt.show()


#Tukey HSD test
def t_hsd(dFrame):
    dFrame = melt(dFrame)
    print(pairwise_tukeyhsd(dFrame['Värde'], dFrame['Navigeringsmetod']))

#Help function
def help(message = ""):
    print("*"*50)
    if message != "":
        print(message)
    print("Usage: python3 analysisTools.py <file> <argument> <plot title>")
    print("Arguments: box, qq, shapiro, anova, t_hsd, resid")
    print("*"*50)
    exit()

#Driver code
if __name__ == '__main__':
    #read file into pandas dataframe
    dFrame = None
    if len(sys.argv) > 1:
        #if first arg is help
        if sys.argv[1] in ['h', 'help', '-h', '--help']:
            help()
        #if the file doesnt exist
        try:
            dFrame = pd.read_csv(sys.argv[1], sep="\t")
        except FileNotFoundError:
            #if file doesnt exist
            help("File not found")
    else:
        #if no file is given
        help("No file given")
    #check if argument is given and running cooresponding function
    if len(sys.argv) > 2:
        if sys.argv[2] == 'box':
            if len(sys.argv) > 3:
                boxPlot(melt(dFrame), sys.argv[3])
            else:
                boxPlot(melt(dFrame))
        elif sys.argv[2] == 'qq':
            if len(sys.argv) > 3:
                qq(dFrame, sys.argv[3])
            else:
                qq(dFrame)
        elif sys.argv[2] == 'histo':
            if len(sys.argv) > 3:
                histogram(dFrame, sys.argv[3])
            else:
                histogram(dFrame)
        elif sys.argv[2] == 'shapiro':
            shapiro(dFrame)
        elif sys.argv[2] == 'anova':
            anova(dFrame, True)
        elif sys.argv[2] == 't_hsd':
            t_hsd(dFrame)
        elif sys.argv[2] == 'resid':
            if len(sys.argv) > 3:
                resid(dFrame, sys.argv[3])
            else:
                resid(dFrame)             
        else:
            #if no valid argument is given
            help("Invalid argument given")
    else:
        #if no argument is given
        help("No argument given")
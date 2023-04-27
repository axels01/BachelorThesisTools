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
import csv
import matplotlib.pyplot as plt


#Simple file reader
def readFile(fileName):
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(float(row[0]))
    return data

#creates a normal distribution graph from the data in the file
#has default values for title, x and y labels and bins which can
#be changed by the user if the initial graph looks good
def normalDistrivution(fileName, title="Normal distribution", xlabel="X", ylabel="Y", bins=10):
    data = readFile(fileName)
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


if __name__ == '__main__':
    #prints cwd as a reminder to the user where the script is looking for files
    print("cwd: " + os.getcwd())
    fileName = input("CSV file name (no spaces): ")

    #if the file does not exist, exit the script
    if not os.path.exists(fileName):
        sys.exit("The file does not exist")

    #creates a normal distribution graph from the data in the file
    normalDistrivution(fileName)
    #if the user wants to change the graph, they can do so here
    title = input("Title of graph: ")
    xlabel = input("X label: ")
    ylabel = input("Y label: ")
    normalDistrivution(fileName, title, xlabel, ylabel)
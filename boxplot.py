import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read data into pandas frame
dframe = pd.read_csv("time.csv", sep="\t")
print(dframe) 

#Turns data (dframe) into usable format for seaborn 
meltedDframe = pd.melt(dframe.reset_index(), id_vars=['index'], value_vars=['V', 'S','T'])

#Changes column names 
meltedDframe.columns = ['index', 'Navigeringsmetod', 'Värde']

#Plots data, first row draws the boxplot, second row inserts the dots (data points)
ax = sns.boxplot(x='Navigeringsmetod', y='Värde', data=meltedDframe)
ax = sns.swarmplot(x="Navigeringsmetod", y="Värde", data=meltedDframe)

plt.show()
plt.savefig("time.csv.png")



if __name__ == '__main__':
    pass    
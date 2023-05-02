# BachelorThesisTools
A set of custom-made tools for mine and [Slothmeister95](https://github.com/Slothmeister95)  bachelor thesis project.

## File Tree Generator (generateFileTree.py)
As part of the experiment a file tree was required, this script will generate a file tree at a desired location, several variables of the tree are editable via the last row of the script.

```Python
    makeFileTree(root_path, 2, 4, (6,25), 8, (14,25))
```
The variables and their corresponding action are explained in acomment above the *makeFileTree* function.
## Personal Code Genrator (gnereatePersonalCode.py)
A simple script to generate anonymous codes when conducting the experiment as to make the collected data anonymous. The codes follow the format XYZ-123, however this can be changed via the last line in the script.
```Python
    print(generateCode(3, 3, '-'))
```
It will however only output ascii uppercase characters followed by digits unless further modified.
## Analysis Tools (analysisTools.py)
### Depends on the following:
* [Pandas](https://pandas.pydata.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Scipy](https://scipy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Statsmodels](https://www.statsmodels.org/stable/index.html)

### Implements the following functions:
* Boxplot - for the entire data set, one box per index.
* Q-Q plot - A simple Q-Q plot, will generate one per index.
* Histogram - Will generate one per index.
* Shapiro-Wilks test - Only outputs W- and p-values to console, one line per index.
* Anova - *Not complete.*
* Residual Q-Q - *Not complete.*
* Pairwise Tukey HSD - *Not complete.*

### Input Data and Usage
Usage: *python3 analysisTools.py \<file> \<argument> \<plot title>*

Arguments: *box, qq, shapiro, anova, t_hsd, resid*

The input data is currently configed to follow a specific format, that of three columns, V, S and T spaced by one tab. See the test.data file for an example file. Not that the tab is imporatant and issues arose when trying to edit the file in Visual Studio Code as it seems to insert spaces and not tab.
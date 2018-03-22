# Material-Test-Data-Smoothing
## Read Me
Material Testing Data Smoothing (MTDS), using python code, reads in data from composite material tests. Currently, it only works for coupon level test that measure force, displacement, and strain. 
From these data files smoothened stress strain curves are created,then from these stress strain curves the
Young's Modulus and peak loads can be clearly located. The stress-strain behavior of composite is brittle so the trend 
of these stress-strain curves is mostly linear (this is the elastic response) but they also contain a nonlinear 
portion. That is why Youngs Modulus is found using the begining portion of the stress-strain curve. Deviation from the linear portion(which is found using a linear polynomrial fit of the initial data set). More intense analysis of the stress strain behavior will be later added. Currenly only coupon test and only the Young's modulus is calculated from the data files.

## What is included
- MTDS.py 
- excel file with test speciem paramters
- folder with test data

## Modules used:
- time
- sys
- pylab 
- matplotlib.pyplot
- pandas
- numpy
- math
- os 
- re
- sys
- ExcelWriter (`pip install openpyxl`)

## How to run code:
1. First, make sure that the excel file is filled out with test name and other geometric properties needed.( Look at Input_specs.xlsx for formating.)
2. Inside python 3 environment, run the following sample command:

```
python MTDS.py coupon Input_specs.xlsx 1
```
where

- arg 1: MTDS.py main code that has functions and analysis
- arg 2: this is a flag that tells the code the type of test, i.e. coupon, joint (element), or component level (current version only allows for coupon)
- arg 3: excel file that contains specifications about the test speciemens such as file name and geometry properties
- arg 4: this is another flag that shows tells the code the level of analysis to be performed on the data. Currently only 1 (basic analysis that find the Young's Modulus). The intent of this is to later add in different types of anaylsis, which will produce desired outputs from the input test data. 

## Output
- a new directory named Output with PDF figures of the stress-strain curves of the orgingal and corrected data are plotted.
- an excel file `Output.xlsx` will be created with the output (i.e. Young's Modulus) of for each data file.


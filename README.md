# Material-Test-Data-Smoothing
## Read Me
Material Testing Data Smoothing (MTDS), using python code, composite material testing measures force, displacement, and time. 
From these data files smoothened stress strain curves are wanted. From these stress strain curves the
Young's Modulus and peak loads are wanted. The stress-strain behavior of composite is brittle so the trend 
of these stress-strain curves is mostly linear (this is the elastic response) but they also contain a nonlinear 
portion. That is why Youngs Modulus is found using the begining portion of the stress-strain curve. Deviation from the linear portion(will be found using a linear polynomrial fit). Certain user parameters such as percent of strain to choose portion of curve that is linear. Prior knowledge of type of data that is being read is used to find modulus. For example, knowing that a data file for the testing of a polymer matrix composite material in tension in the fiber direction is highly linear whereas a shear testing is highly non-linear. 

## What is needed
- python 3 
- MTDS.py 
- excel file with test speciem paramters
- folder with test data


## Directory naming 


## How to run code:
1. First, make sure that the excel file is in the local directory as siofinal.py and directory with test data.
2. inside python 3 environment the following command sample command shows how to run the code:

```
python MTDS.py coupon Input_specs.xlsx 1
```
- arguement 1: MTDS.py main code that has functions and analysis
- arguement 2: this is a flag that tells the code the type of test, i.e. coupon, joint (element), or component
- arguement 3: excel file that contains specifications about the test speciemens such as file name and geometry properties
- arguement 4: this is another flag that shows tells the code the level of analysis to be performed on the data. Currently only 1 (basic analysis that find the Young's Modulus). The intent of this is to later add in different type anaylsis depending on the outputs desired from the input test data. 


############################################################
#                                                          #
# Import modules used for in this script                   #
#                                                          #
############################################################
import time
start_time = time.time()
import sys
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os 
import re
from sys import argv
from pandas import ExcelWriter

############################################################
#                                                          #
# Functions for Data input check                           #
#
############################################################
#function to check if all inputs are correctly inputed

def test_check(type_test):
	test_types = ['Coupon', 'Joint','Component']
	answer = type_test 
	while True:
		if any(item.lower() == answer.lower() for item in test_types): 
			break
		print("****ERROR: Incorrect Input foe Testing Type****")
		print("Available: Coupon, Joint, Component.")
		sys.exit()
		return answer

def analysis_check(analysis_output):
	answer = analysis_output
	if answer > 3:
		print("****ERROR: Incorrect Input foe Analysis Type****")
		print("You must select a number from 0 to 3.")
		sys.exit()
		return answer

############################################################
#                                                          #
# Functions for Data Processing                            #
#                                                          #
############################################################

def CouponAnalysis(type_test,excel_input):
	CouponSpecs = pd.read_excel(excel_input,sheet_name='Coupon')# Read the excel file and fix data 
	#CouponSpecs = pd.read_excel('../final/CouponData/SE171 WI2017.xlsx')
	input_pwd = os.getcwd()
	#input_data = '~/sio209/final/CouponData/'#path of the data, use global
	# CouponSpecs = CouponSpecs.iloc[5:]###This is specific for this excel file, take it out
	#this should never be here
	CouponSpecs['Area'] = CouponSpecs.Thickness*CouponSpecs.Width
	CouponSpecs= CouponSpecs.reset_index()
	t=CouponSpecs.Note.notnull()
	tt = [i for i, x in enumerate(t) if x]
	tt=(np.array(tt))
	for i in tt:
		CouponSpecs = CouponSpecs.drop(i)
	CouponSpecs =CouponSpecs.reset_index()
	# Now using the data from excel, now stored as pandas dataframe use to open
	# the test data
	input_filenames  = CouponSpecs.Coupon.values
	addpath = input_pwd +'/CouponData/'
	input_filename = [addpath+i +'.'+ input_format for i in input_filenames]
	return (CouponSpecs,addpath,input_filename,input_filenames)

def BasicAnalysisCoupon(analysis_output,CouponSpecs,input_filename,input_filenames):
	df.columns = ['Crosshead','Load','Time','Extensometer']
	#create figure and axis
	# This is where the function that fixes the data goes
	#get columns of data that will be plotted
	x_og = np.array(df['Extensometer']) #x-axis data
	y_og = np.array(df['Load']/area_average) #y-axis data 
	#call function to correct data
	(stress,extenso)=CouponCorrection(x_og,y_og)
	x = np.array(extenso);
	y = np.array(stress);
	# print(x[0])
	# print(y[0])
	# birange=math.ceil(len(x)*percentbias)
	aa=np.median(extenso)
	b=find(extenso < aa)
	birange = b[-1]
	
	# load_max =	CouponSpecs['Peak Load [lbs]'].iloc[0]/area_average
	#str(round(numvar,9))
	m,b = np.polyfit(x[1:15], y[1:15], 1);
	# print(b)
	df_calcs[input_filenames[i]] = [m]
	#figure labels
	# plt.cla()
	# plt.clf()
	fig, axes = plt.subplots(nrows=2, ncols=1)
	axes[1].plot(x, y, color="r")  
	axes[1].plot(x[1:birange],m*x[1:birange]+b,color='b')
	axes[1].set_xlabel('Engineering Strain')
	axes[1].set_ylabel('Engineering Stress [psi]')#note the units are hard coded
	# axes[1].set_ylim([0, 1.1*np.max(y)])
	# axes[1].set_xlim([0, 1.1*np.max(x)])
	axes[1].set_title('Corrected:'+input_filenames[i]);
	# plt.annotate(
	# 	'Max Load:'+ str(load_max),
	# 	xy=(x[-1], np.max(y)), xytext=(np.random.randint(10,15),np.random.randint(30,40)),
	# 	textcoords='offset points', ha='left', va='top',
	# 	bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
	# 	arrowprops=dict(arrowstyle = '->', connectionstyle='arc,rad=0'))
	
	# axes[1].plot(x, y, color="r")  
	axes[0].plot(x_og,y_og,color='k')
	axes[0].set_xlabel('Strain')
	axes[0].set_ylabel('Stress')
	axes[0].set_title('Original:'+input_filenames[i]);
	# axes[0].set_ylim([0, 1.1*np.max(y_og)])
	# axes[0].set_xlim([0, 1.1*np.max(x_og)])
	fig.tight_layout()
	newpath = os.getcwd() + '/Output/'
	filename_out = newpath+input_filenames[i] + '.pdf';

	return x,y,fig, df_calcs,filename_out

def CouponCorrection(x_og,y_og):
	# stress_0 = y_og[0];
	# extenso_0 = x_og[0];
	# #print(stress_0)
	# stress = y_og-stress_0;
	# extenso = x_og-extenso_0;
	stress = y_og;
	extenso = x_og;
	#new correction using the difference between two points and the median value, then find the indices
	#of where the differnece is greater than the median.
	test_diff = np.diff(extenso)
	threshold = np.average(test_diff)
	indices = np.where(test_diff > threshold)
	datalim = indices[0][0]-1

	stress_1 = stress[1:datalim]
	extenso_1 = extenso[1:datalim]
	stress_0 = stress_1[0];
	extenso_0 = extenso_1[0];
	#print(stress_0)
	stress_2 = stress_1 - stress_0;
	extenso_2 = extenso_1 - extenso_0;

	#old way of correction
	# slopes = np.diff(stress[1:])/np.diff(extenso[1:])
	# jumppy = np.where(slopes < 0)
	# # print(jumppy)
	# jumppy = np.array([i+1 for i in jumppy])
	# # print(jumppy)
	# stress = [i for i,j in zip(stress,range(len(stress))) if j not in jumppy[0]]
	# extenso = [i for i,j in zip(extenso,range(len(extenso))) if j not in jumppy[0]]
	# #len(stress)
	# strain_jump = np.where(np.diff(extenso)<0);
	# # strain_jump = strain_jump[0]
	# strain_jump = np.array([i+1 for i in strain_jump])

	# stress = [i for i,j in zip(stress,range(len(stress))) if j not in strain_jump[0]]
	# extenso = [i for i,j in zip(extenso,range(len(extenso))) if j not in strain_jump[0]]
	# #print(len(strain_jump[0]))
	# stress_jump = np.where(np.diff(stress)<0);
	# stress_jump = np.array([i+1 for i in stress_jump])
	# stress = [i for i,j in zip(stress,range(len(stress))) if j not in stress_jump[0]]
	# extenso = [i for i,j in zip(extenso,range(len(extenso))) if j not in stress_jump[0]]
	# #print(len(stress_jump[0]))
	# strain_lim = np.where( np.array(extenso) > 0.19)#this number is an appropriate strain lim
	# stress = [i for i,j in zip(stress,range(len(stress))) if j not in strain_lim[0]]
	# extenso = [i for i,j in zip(extenso,range(len(extenso))) if j not in strain_lim[0]]
	return stress_2,extenso_2

# def LapAnalysis(type_test,excel_input):
	# CouponSpecs = pd.read_excel(excel_input,sheet_name='Lap')# Read the excel file and fix data 
	# input_pwd = os.getcwd()
	# CouponSpecs['Area'] = CouponSpecs.Thickness*CouponSpecs.Width
	# CouponSpecs= CouponSpecs.reset_index()
	# t=CouponSpecs.Note.notnull()
	# tt = [i for i, x in enumerate(t) if x]
	# tt=(np.array(tt))
	# for i in tt:
	# 	CouponSpecs = CouponSpecs.drop(i)
	# CouponSpecs =CouponSpecs.reset_index()
	# # Now using the data from excel, now stored as pandas dataframe use to open
	# # the test data
	# input_filenames  = CouponSpecs.Coupon.values
	# addpath = input_pwd +'/LapData/'
	# input_filename = [addpath+i +'.'+ input_format for i in input_filenames]
	# return (CouponSpecs,addpath,input_filename,input_filenames)


############################################################
#                                                          #
# Main script                                              #
#                                                          #
############################################################

print("""
############################################################
#                                                          #
# Composite Material Test Data Analysis                    #
#                                                          #
############################################################
""")
# Inputs arguments
script = argv[0]
type_test = argv[1]
excel_input = argv[2]
analysis_output = int(argv[3]) # this is a flag to perform basic analysis for this class
# but can be expanded to more detailed analysis extraction from the input files
# %matplotlib inline
input_format = 'txt'; # this part will later be an arg

# functions that check corrct inputs
analysis_check(analysis_output)
test_check(type_test)

# print what is done
print("script: %s\nTest Type: %s\nAnalysis Type: %s\n" % (script, type_test, analysis_output))

############################################################
#                                                          #
# Coupon Analysis                                          #
#                                                          #
############################################################
(CouponSpecs,addpath,input_filename,input_filenames) =CouponAnalysis(type_test,excel_input)
if analysis_output == 1:
	calcs = ['Modulus [psi]'];
	# gage_length = 5.5;#inches, this is something can change
	df_calcs =  pd.DataFrame(index=calcs,columns=input_filenames)
	percentbias = 0.05;
	# create empty data frame to store youngs modulus of each test
	# note to make the title of the figure, use grep to get the filename before .txt
	# using all the runs for each case, use the stats to create estimates of the optimal/average or some sort of statistical
	for i in range(len(input_filename)):
		# print(i)
		area_average = CouponSpecs.Area.iloc[i];# inches
		df = pd.read_csv(input_filename[i],index_col=None,sep='\t',header=5)
		(x,y,fig, df_calcs,filename_out)=BasicAnalysisCoupon(analysis_output,CouponSpecs,input_filename,input_filenames)
		newpath = os.getcwd() + '/Output/'
		# newpath = 
		if not os.path.exists(newpath):
			os.makedirs(newpath)

		fig.savefig(filename_out)#save file as PDF
		plt.close()
		dataout = {'strain': x, 'stress':y}
		dfout = pd.DataFrame(dataout)
		outfile = newpath +'corrected-'+input_filenames[i]+'.txt'
		dfout.to_csv(outfile,sep=' ', index=False,header=True)
		# print(addpath)
		# resultss[i] = df_calcs
	# print(df_calcs)
	#save the corrected stress and strain to new file

	writer = pd.ExcelWriter('output.xlsx')
	df_calcs.to_excel(writer,'Sheet1')
	writer.save()
elif analysis_output == 2:
		print('More intense analysis')

print('Figures and Processed Data saved to: %s' %newpath )
############################################################
#                                                          #
#  Joint Analysis                                          #
#                                                          #
############################################################


############################################################
#                                                          #
#   Bolt Analysis                                          #
#                                                          #
############################################################


#
print("--- %s seconds ---" % (time.time() - start_time))


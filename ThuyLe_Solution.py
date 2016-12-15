# -*- coding: utf-8 -*-
"""
Oval code-quiz ThuyLe solution
Created on Thu Dec 15 14:41:06 2016

@author: eleethy
"""

#==============================================================================
# import libraties
#==============================================================================
import os
import pandas as pd


#==============================================================================
# Function load data from a file
# input:
#    _fileName: Name of a file
# output
#   Data_df: Data of the a (type: DataFrame)
#==============================================================================
def LoadData(_fileName):
    Data_df = pd.read_csv(_fileName)
    return Data_df

    
#==============================================================================
# Function find single customers
# input:
#    _listCust: List all customers go to party
# output
#   _listCust: List all customers whose go to party alone (type: list)
#==============================================================================
# Solution 1, use two for loops => Suitable with small data
def CheckSingle1(_listCust):
   listRemove =[]
   for i in range(0, len(_listCust)-1):
        for j in range(i+1, len(_listCust)):
            #Check couple customers 
            if (_listCust[i]==_listCust[j]):
                #Add item to listRemove
                listRemove.append(_listCust[i])
                listRemove.append(_listCust[j])
                
   for item in listRemove:
        _listCust.remove(item)

   return _listCust

# Solution 2, use one for loops, use one more list => Suitable with big data
def CheckSingle2(_listCust):
   singleCustomers =[]
   for item in _listCust:
       if (item not in singleCustomers):
           singleCustomers.append(item)
       else:
           singleCustomers.remove(item)

   return singleCustomers

# Solution 3, use one for loops, use Set
# => Suitable with big data, Should use this function
def CheckSingle3(_listCust):
   singleCustomers = set([])
   for item in _listCust:
       if (item not in singleCustomers):
           singleCustomers.add(item)
       else:
           singleCustomers.remove(item)

   return singleCustomers

   
#==============================================================================
# Function analyst data of the file 
# input:
#    _filename: Name of a file
# output
#   resultdf: List all customers whose go to party alone (type: DataFrame)
#==============================================================================
def DataAnalyst(_inputFileName, _outputFileName):
    data = LoadData(_inputFileName)
    N = data.columns.tolist()[0]
    data = data[N]
    case=0
    result = []
    while (case < int(N)):
        # Number of guests
        #G = data[2*case] #=> Don't use this information

        # List of Customers
        listCustomers = data[2*case+1].split(' ')
        case = case+1
        listSingleCustomers = CheckSingle3(listCustomers)
        out = 'Case #' + str(case) 
        for item in listSingleCustomers:
            out = out + ' ' + str(item)
        result.append(out)
    resultdf = pd.DataFrame(result)
    resultdf.to_csv(_outputFileName, index=False, header=False)
    return resultdf
    

#==============================================================================
#  Function use to analyst all files
#==============================================================================
# Declare variables
#### Have to modifie suitable with user
data_location = 'C:/Users/eleethy/Desktop/Ovan case study/code-quiz-master/'
inputFileName1 = "oval-quiz-sm.in"
inputFileName2 = "oval-quiz-lg.in"

outputFileName1 = "oval-quiz-sm.out"
outputFileName2 = "oval-quiz-lg.out"

# Set the current working directory 
os.chdir(data_location)

#==============================================================================
# Data Analyst
#==============================================================================
DataAnalyst(inputFileName1, outputFileName1)
DataAnalyst(inputFileName2, outputFileName2)
 

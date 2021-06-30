#Created by Luis Madrid

import pandas as pd
import numpy as np
import glob
import tkinter as tk
import os
import sys

dir_loc = os.path.dirname(__file__)
dir_save = dir_loc[:-7]

#FUNCTION MERGE TABLE AND ELEMENT INPUT
def gen_dataframe(arrEid, request_data, df_all_final, name_col, p_update, elm_val):

    #empty DataFrame to store final values from critica FI for each element
    outputDf = pd.DataFrame()
    dummy_number = 0
    total_elements = len(arrEid)
    catch_list = []
    #Loop thru each arrEid, and create a new DataFrame with Maximum FI.
    if request_data == 'Maximum':
        for elm in arrEid:
            try:
                trial2 = df_all_final.loc[df_all_final[elm_val].isin([elm])]
                maxElmFi = max(trial2[name_col])
                idxElmFi = trial2.loc[trial2[name_col] == maxElmFi]
                outputDf = pd.concat([outputDf,idxElmFi], ignore_index = True)

                #PROGRESS BAR INFO
                dummy_number = dummy_number + 1
                p_update['value'] = (dummy_number/float(total_elements)) * 100
                p_update.start
                p_update.update()
            except:
                catch_list.append(elm)

    elif request_data == 'Minimum':
        for elm in arrEid:
            try:
                trial2 = df_all_final.loc[df_all_final[elm_val].isin([elm])]
                maxElmFi = min(trial2[name_col])
                idxElmFi = trial2.loc[trial2[name_col] == maxElmFi]
                outputDf = pd.concat([outputDf,idxElmFi], ignore_index = True)

                #PROGRESS BAR INFO
                dummy_number = dummy_number + 1
                p_update['value'] = (dummy_number/float(total_elements)) * 100
                p_update.start
                p_update.update()
            except:
                catch_list.append(elm)

    #Export DataFrame into a CSV file
    p_update.stop
    outputDf.to_csv(dir_save + "Downselect_ "+ name_col +"_"+ request_data +".csv", index = False, header = True)

    return catch_list

#ELEMENT INPUT FROM USER TO NUMERIC LIST
def elm_input(elm_text_str):
    # Function to convert text elm, to list in numeric values
    user_list = elm_text_str.split('\n')

    #Removes while spaces between elements
    while ("" in user_list):
        user_list.remove("")

    #convert each item to int type
    for i in range(len(user_list)):
        #convert each item to int type
        user_list[i] = int(user_list[i])

    return user_list

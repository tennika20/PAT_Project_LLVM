import matplotlib.pyplot as plt
import csv
import glob
import os
from matplotlib.pyplot import figure
import pandas as pd

current_dir=os.getcwd()
csvdir=current_dir+"/csv_data"
def addlabels(x: object, y: object) -> object:
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
#plot 1
def Plot1():
    df_aggregated_assert_count = pd.read_csv(csvdir+"/assertCountOnFolderLevel.csv")
    plt.figure(figsize=(5,10))
    plt.xlabel("DIR Location")
    plt.ylabel("Number of Asserts")
    plt.title("Aggregated Assert Count for each directory", loc='center')
    plt.bar(x=df_aggregated_assert_count['outer_location'], height=df_aggregated_assert_count['AssertCount'], align="center")
    plt.xticks(rotation=90)
    plt.savefig('assertcount.png')

def Plot2():
    df_assert_and_debug_count=pd.read_csv(csvdir+"/Folder_Assert_Debug_Count.csv")
    print(df_assert_and_debug_count.head(10))
    plt.figure(figsize=(5,10))
    plt.xlabel("DIR Location")
    plt.ylabel("Count of Assert and Debug Statements")
    plt.title("Assert and Debug Count for each directory", loc='center')
    #plt.bar(x=df_assert_and_debug_count['outer_location'], height=df_assert_and_debug_count['AssertCount'], label="assert")
    #addlabels(df_assert_and_debug_count['outer_location'],df_assert_and_debug_count['AssertCount'])
    plt.bar(x=df_assert_and_debug_count['outer_location'], height=df_assert_and_debug_count['DebugCount'], label="debug")
    addlabels(df_assert_and_debug_count['outer_location'],df_assert_and_debug_count['DebugCount'])
    plt.xticks(rotation=90)
    plt.savefig('assertanddebug.png')

def Plot3():
    unit_test=[6712,6705,0,0,7]
    tests=['total','passed','unsupported','failed','skipped']
    plt.xlabel('Test Results')
    plt.ylabel('Number of tests')
    plt.title('Test Results for Unit Test-Suite',loc='center')
    plt.bar(tests,unit_test)
    addlabels(tests,unit_test)
    plt.xticks(rotation=0)
    plt.savefig('unitsuite.png')


def Plot4():
    regression_test=[48233,47548,518,160,7]
    tests=['total','passed','unsupported','failed','skipped']
    plt.xlabel('Test Results')
    plt.ylabel('Number of tests')
    plt.title('Test Results for Regression Test-Suite',loc='center')
    plt.bar(tests,regression_test)
    addlabels(tests,regression_test)
    plt.xticks(rotation=0)
    plt.savefig('regressionsuite.png')

Plot1()
Plot2()
Plot3()
Plot4()





import pandas as pd
import os

def assert_aggCSV():
        dir_store=os.getcwd()
        dir_store=dir_store+"/csv_data/"
        data=pd.read_csv(dir_store+"aggregation_count.csv")
        all=[]
        series = data["AssertCount"]
        File_Locations = data["Location"]
        for f in range(len(File_Locations)):
            folder_name=File_Locations[f]
            folder_name=folder_name.split("/")[1]
            all.append(folder_name)

        data['outer_location'] =all
        data_grouped=data.groupby('outer_location').sum()
        data_grouped.to_csv(dir_store+"assertCountOnFolderLevel.csv")


def assertdebugCSV():
        dir_store=os.getcwd()
        dir_store=dir_store+"/csv_data/"

        data=pd.read_csv(dir_store+"assert_debug.csv")
        all=[]

        series = data["AssertCount"]
        File_Locations = data["Location"]
        for f in range(len(File_Locations)):
            folder_name=File_Locations[f]
            # print(folder_name)
            folder_name=folder_name.split("/")[1]

            all.append(folder_name)

        data['outer_location'] =all
        data_grouped=data.groupby('outer_location').sum()

        data_grouped.to_csv(dir_store+"Folder_Assert_Debug_Count.csv")



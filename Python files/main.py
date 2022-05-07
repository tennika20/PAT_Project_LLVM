import os
import re
import time 
from partthree import *
from assert_agg import *
from gen-figures1 import *
from gen-figures2 import *
import subprocess 



if __name__=="__main__":
    csv_files_rm=os.system('rm -rf csv_data')
    csv_files_dir=os.system('mkdir csv_data')
    figures_rm=os.system('rm -rf Figures')
    figures_dir=os.system('mkdir Figures')
    GEN_CSV_Assert()
    ASSERTNDEBUG()
    assertdebugCSV()
    assert_aggCSV()
    subprocess.run(['python','./PythonFiles/PyDrillerScript.py'])
    outDrillerCSV()
    os.system(figures_rm)
    os.system(figures_dir)
    subprocess.run(['python','./PythonFiles/pydriller.py'])
   

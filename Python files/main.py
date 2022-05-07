import os
import re
from partthree import *
from assert_agg import *
from gen_data_pre import *



if __name__=="__main__":
    os.system('rm -rf csv_data')
    os.system('mkdir csv_data')
    GEN_CSV_Assert()
    ASSERTNDEBUG()
    assertdebugCSV()
    assert_aggCSV()

    



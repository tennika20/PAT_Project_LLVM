# 3- the number and location of the debug and assert statements in production files.
import os
import re
def ASSERTNDEBUG():
   
    removefile="rm dump_assertndebug.txt"

    


    command='grep -r  --include="*.py" --include="*.c" --include="*.cpp" -n -E  "((.*@test.*)|(EXPECT_)| {3,}assert\w*)|(DEBUG_ASSERT\(.*\))|Debug|(\.debug\()" --exclude=main.py --exclude=partthree.py --exclude=assert_agg.py  --exclude=gen_data_pre.py --exclude="*test*.py" --exclude-dir={test,tests,testing,venv,unittests} >> dump_assertndebug.txt  '


    os.system(removefile)                       
    os.system(command)
    preprocess_strings()
    

def preprocess_strings():
    assert_lineno_str=""
    debug_lineno_str=""
    TT_FIL_Assert=0
    Total_asserts=0
    prev_file="NA"
    Total_debug_statements=0
    Total_debug_statements_in_all_files=0
    file=open("./dump_assertndebug.txt")
    resultfile= open("./csv_data/assert_debug.csv", "w")
    resultfile.write('Location,Assertlineno,Debuglineno,AssertCount,DebugCount\n')
    TTF=0
    for f in file:
        
        File_attr =f.split(":",2)
        file_name=File_attr[0]
        line_no=File_attr[1]
        line=File_attr[2]
        if(prev_file==file_name):
            if(re.search("assert",line)):
                Total_asserts+=1
                TT_FIL_Assert+=1
                assert_lineno_str=assert_lineno_str+" "+line_no
            if(re.search("debug",line,re.IGNORECASE) or re.search("expect_",line,re.IGNORECASE) or re.search(".*@test",line,re.IGNORECASE)):
                Total_debug_statements+=1  
                Total_debug_statements_in_all_files+=1 
                debug_lineno_str=debug_lineno_str+" "+ line_no

        elif(prev_file!=file_name):
            
            TTF+=1
            if(Total_asserts>0 or Total_debug_statements>0):
                
                resultfile.write("\""+assert_lineno_str+"\""+",")
                resultfile.write("\""+debug_lineno_str+"\"")
                assert_lineno_str=""
                debug_lineno_str=""
                resultfile.write(","+str(Total_asserts))
                resultfile.write(","+str(Total_debug_statements)+"\n")
            Total_asserts=0
            Total_debug_statements=0
            resultfile.write(file_name+",")
            
            prev_file=file_name
            
            if(re.search("assert",line)):
                Total_asserts=1
                TT_FIL_Assert+=1
                assert_lineno_str=""+line_no
            if(re.search("debug",line,re.IGNORECASE) or re.search("expect_",line,re.IGNORECASE) or re.search("test",line,re.IGNORECASE)):
                Total_debug_statements=1   
                Total_debug_statements_in_all_files+=1 
                debug_lineno_str=""+line_no 
    resultfile.write("\""+assert_lineno_str+"\""+",")
    resultfile.write("\""+debug_lineno_str+"\"")    
    resultfile.write(","+str(Total_asserts))
    resultfile.write(","+str(Total_debug_statements)+"\n")


    print("\n" +"debug and assert statements files: "+str(TTF)+"\n")    
    print("\n" +"Debug statements in all files: "+str(Total_debug_statements_in_all_files)+"\n")    
    print("\n" +"Asserts statements in in all files: "+str(TT_FIL_Assert)+"\n")  
    file.close()        
        


    

       
        
        

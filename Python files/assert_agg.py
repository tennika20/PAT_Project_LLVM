# 2- the number for test files and the number of assert statements in each file
import os

def GEN_CSV_Assert():
    Tot_Asserts=0
    prev_file="NA"
    TF_asserts=0
    removefile="rm dump_assert.txt"
    removedir="rm alltestdirectories.txt"
    textDirCommand='find . -type d -regex ".*tests.*" >> alltestdirectories.txt'
    os.system(removedir)
    os.system(textDirCommand)
    testdirectories=open('./alltestdirectories.txt')
    os.system(removefile)

    for T in testdirectories:
       
        command='grep -r --include="*.cpp" --include="*.c" --include="*.py" --include="*.ll" -E  "(EXPECT_)|(.*@test.*)|( {3,}assert * [A-Za-z]+\.[A-Za-z_]*)|(assert.*==)|(assert.*!=)|(assert.*[><][A-Za-z0-9])|(assert.* is .*)|(assert\(.*;)" '+ T[:-1]  +'/ -n ' +' --exclude="*.dmp" --exclude="*.o"   --exclude=main.py --exclude=partthree.py --exclude=assert_agg.py >> dump_assert.txt'
        # print(command)
        os.system(command)
    file=open("./dump_assert.txt")
    output= open("./csv_data/aggregation_count.csv", "w")
    output.write('Location,Assertlineno,AssertCount\n')
    TotalTestFiles=0
    preprocessdata(prev_file,file,TotalTestFiles,TF_asserts,Tot_Asserts,output)
   


def preprocessdata(prev_file,file,TotalTestFiles,TF_asserts,Tot_Asserts,output):
    for f in file:
        
        file_detail =f.split(":",2)
        Fl_name=file_detail[0]
        # print(file_detail)
        line_no=file_detail[1]
        # print(line_no)
        
        if(prev_file==Fl_name):
            output.write(" "+str(line_no))
            Tot_Asserts+=1
            TF_asserts+=1

        elif(prev_file!=Fl_name):
            TotalTestFiles+=1
            TF_asserts+=1
            if(Tot_Asserts>0):
                output.write("\""+",")
                output.write(str(Tot_Asserts)+"\n")
            Tot_Asserts=1
            prev_file=Fl_name
            output.write(Fl_name)
            output.write(","+"\"")
            output.write(" "+str(line_no))
   
    print("Total Asserts found "+str(TF_asserts))
    output.write("\""+","+str(Tot_Asserts))

    print("\n" +"Total Test Files: "+str(TotalTestFiles)+"\n")    
    # print("worked")
    file.close()        
        




        

        
            
            

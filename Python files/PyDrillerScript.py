from pydriller import Repository
from datetime import datetime
import re
import os
#dir = os.getcwd()

output= open("PydrillerDetails.csv", "w")
output.truncate(0)
date1 = datetime(2022, 1, 8, 16, 0, 0)
date2 = datetime(2022, 5, 8, 16, 0, 0)
for commit in Repository('https://github.com/llvm/llvm-project.git', since=date1, to=date2).traverse_commits():
    for file in commit.modified_files:
        if(re.search('test',file.filename)):
                #print("File {} is change_type {} is modified by author {} at committer_date {}".format(commit.filename, commit.change_type,commit.author.name,commit.committer_date))
                output.write(commit.filename+","+commit.change_type+","+commit.author.name+","+commit.committer_date+"\n")
output.close()
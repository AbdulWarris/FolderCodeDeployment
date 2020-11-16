import os, shutil
import sys
import argparse
import datetime
import distutils
from distutils import dir_util

#     "compare_dir_layout
#     Compare two directories recursively. Files in each directory are
#     assumed to be equal if their names and contents are equal.
#     @param mParam_dSrc: First directory path as Source
#     @param mParam_dDes: Second directory path as Destination
#     @param mParam_dirBackup: A Log directory path as Log file having all destination file and folder
#            exisit inside source and destination
#     @return: True if the directory trees are the same and 
#         there were no errors while accessing the directories or files, 
#         False otherwise.
def compareAndCopy_dir_process(mParam_dSrc, mParam_dDes,mParam_dirBackup):
    def _compareAndCopy_dir_process(mParam_dSrc, mParam_dDes,mParam_dirBackup):
        try:
            for (mVar_DirPath, mVar_Dirnames, mVar_Filenames) in os.walk(mParam_dSrc):
                for ml_filename in mVar_Filenames:
                    ml_relative_path = mVar_DirPath.replace(mParam_dSrc, "")
                    if os.path.exists( mParam_dDes + ml_relative_path + '\\' +  ml_filename) == False:
                        ml_src_file = mParam_dDes + ml_relative_path + '/' +  ml_filename
                        ml_dst_dir = mParam_dirBackup + ml_relative_path
                        if (len(ml_relative_path)!=0):
                            if not os.path.exists(ml_dst_dir):
                                os.makedirs(ml_dst_dir)
                        shutil.copy(ml_src_file, ml_dst_dir)
            return
        except expression as identifier:
            raise identifier

    print 'Backcup Start in folder "' + mParam_dirBackup
    _compareAndCopy_dir_process(mParam_dDes, mParam_dSrc,mParam_dirBackup)
    print 'Backcup Done in folder "' + mParam_dirBackup


# Function to convert   
def listToString(mParam_Str):  
    mVar_Str1 = ""  
    # traverse in the string   
    for eleInStr in mParam_Str:  
        mVar_Str1 += eleInStr   
    return mVar_Str1  
        

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-s','--src', help='This is the help, Here pass --src for Source Directory',type=str,nargs=1)
        parser.add_argument('-d','--des', help='--des for Destination',type=str,nargs=1)
        mVar_args = parser.parse_args()
        mVar_today = datetime.datetime.now()
        mParam_dirBackup= "./log"+mVar_today.strftime('%d%m%Y_%H%M%S')
        # dirSrc = "./test1" # dirDes = "./test2"
        mVar_dirSrc = listToString(mVar_args.src)
        mVar_dirDes = listToString(mVar_args.des)
        print "Backup in process... of destination " + mVar_dirDes + " if exist in src " + mVar_dirSrc 
        if not os.path.exists(mParam_dirBackup):
            os.makedirs(mParam_dirBackup)
        compare_dir_layout(mVar_dirSrc, mVar_dirDes,mParam_dirBackup)
        print "Start Copy in process... of destination folder" + mVar_dirDes 
        distutils.dir_util.copy_tree(mVar_dirSrc,mVar_dirDes)
    except Exception as e:
       print( "Error:"+str(e) ) 

if __name__ == "__main__":
    main()
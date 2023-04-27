'''
Axel Östergren 2023-04-26

This is a short script to generate a random file tree
from a few set perameters. This script is written 
as part of a bachelor thesis project
by Axel Östergren and Arvid Albinsson at Högskolan Väst
in Trollhättan, Sweden.

The script is free to use and can be modified
by anyone. The script is provided as is and the authors
take no responsibility for any damage caused by the script.
'''

import os
import sys
import random
import string

def folderName():
    #Folder name, 8 random digits
    return ''.join(random.choices(string.digits, k=8))


def fileName():
    #File name, 3 random letters, 3 random digits, .dxf extension
    letters = random.choices(string.ascii_uppercase, k=2)
    numbers = random.choices(string.digits, k=3)
    return ''.join(letters + numbers) + '.dxf'


    #root_path, deapth of file tree(counts of folders), 
    #chanse of files in folder, random interval of files in folder, 
    #count of folders in root, random interval of folders not in root
def makeFileTree(root_path, depth, chanseOfFiles, filesInterval, foldersInRoot, foldersInterval, first_call=True):
    if depth == 0:
        if (random.randint(1, chanseOfFiles) != 1):
            return
        else:
            for i in range(random.randint(filesInterval[0], filesInterval[1])):
                file_name = fileName()
                file_path = os.path.join(root_path, file_name)
                open(file_path, 'w').close()
    else:

        if not first_call:
            foldersInRoot = random.randint(foldersInterval[0], foldersInterval[1])
        for i in range(foldersInRoot):
            folder_name = folderName()
            folder_path = os.path.join(root_path, folder_name)
            os.mkdir(folder_path)
            makeFileTree(folder_path, depth - 1, chanseOfFiles, filesInterval, foldersInRoot, foldersInterval, False)

if __name__ == "__main__":
    root_path = input("Path where you want to generate the file tree (path can't contain spaces): ")
    if not os.path.exists(root_path):
        sys.exit("The path does not exist")
    
    makeFileTree(root_path, 2, 4, (6,25), 8, (14,25))




    
from genericpath import isdir, isfile
from itertools import count
import os

def createFile(filename):

    open(filename, 'w')
    print("[+] Generated file "+filename)

def createDirectory(path, foldername):

    os.mkdir(path + foldername + "/")
    print("[+] Generated directory "+ foldername)
    

def generate(folder, task):
    
    path = "C:/Users/Jesus/Documents/SMS-ME/"
    folder = "/" + folder
    task = "/" + task

    if os.path.isdir(path + folder):
        os.chdir(path + folder)
        
    else:
        createDirectory(path,folder)
        os.chdir(path + folder)
        createFile('localhost.txt')

    if os.path.isdir(path + folder + task):
        print("[!] task code already exists!")
        
    else:
            
        createDirectory(path + folder, task)
        os.chdir(path + folder + task)

        createDirectory(path + folder + task, '/urls')

        createFile('issue.txt')
        createFile('updates.txt')
        createFile('queries.txt')
        createFile('conclusion.txt')
        
def generate_only_folders(folder):
    path = "C:/Users/Jesus/Documents/SMS-ME/"
    folder = "/" + folder
    if os.path.isdir(path + folder):
        os.chdir(path + folder)
        
    else:
        createDirectory(path,folder)
        os.chdir(path + folder)
        createFile('readme.txt')